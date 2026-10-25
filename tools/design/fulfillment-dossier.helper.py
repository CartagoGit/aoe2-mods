"""Run the typed fulfillment projector once per authored batch.

The wrapper fails closed when Bun, the bridge, schema validation or accounting
is unavailable. It does not mutate a campaign or manufacture a fallback.
"""

import importlib.util
import json
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
BRIDGE = Path(__file__).with_name("fulfillment-dossier.script.ts")
ALLOCATION_HELPER = Path(__file__).with_name("finite_allocation.helper.py")
LEVELS = ("easy", "standard", "hard")
RESOURCES = ("food", "wood", "gold", "stone")
MAX_SAFE_INTEGER = 2**53 - 1


def _optional_states():
    spec = importlib.util.spec_from_file_location("finite_allocation", ALLOCATION_HELPER)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load finite allocation helper: {ALLOCATION_HELPER}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.optional_states


def _with_optional_analysis(projection, accounts_by_difficulty):
    optional_states = _optional_states()
    inputs = projection["optionalFinancialInputs"]["optionalTasks"]
    output = {}
    for level in LEVELS:
        account = accounts_by_difficulty[level]
        stock = {key: account["spendable"].get(key, 0) for key in RESOURCES}
        _check_safe_balance(stock, f"{level} pre-funding stock")
        states = optional_states(stock, inputs)
        _check_safe_states(states, f"{level} pre-funding analysis")
        after_funding = []
        for selection in projection["selectionAnalysisByDifficulty"][level]["selections"]:
            row = {
                "recipeIds": selection["recipeIds"],
                "mainAffordable": selection["affordable"],
                "initialRemainder": (
                    selection["spendableRemainder"] if selection["affordable"] else None
                ),
                "scope": "after-main-funding",
            }
            if selection["affordable"]:
                remainder = selection["spendableRemainder"]
                _check_safe_balance(remainder, f"{level} funded remainder {selection['recipeIds']}")
                funded_states = optional_states(remainder, inputs)
                _check_safe_states(funded_states, f"{level} after-funding analysis {selection['recipeIds']}")
                all_optional_mask = (1 << len(inputs)) - 1
                row.update({
                    "reachableSubsetCount": len(funded_states),
                    "allOptionalTasksAffordable": all_optional_mask in funded_states,
                    "examples": [
                        {"completedTaskIds": order, "spendableAfterTransfers": balance}
                        for balance, order in funded_states.values()
                    ],
                    "status": "candidate financial prefixes after this main selection; spatial predicates and actor availability are assumed successful",
                })
            else:
                row.update({
                    "reachableSubsetCount": None,
                    "allOptionalTasksAffordable": None,
                    "examples": None,
                    "reason": "main selection is not affordable from initial spendable stock; no after-funding witness",
                })
            after_funding.append(row)
        output[level] = {
            "scope": "before-main-funding",
            "reachableSubsetCount": len(states),
            "allOptionalTasksAffordable": (1 << len(inputs)) - 1 in states,
            "allSkipStock": stock,
            "examples": [
                {"completedTaskIds": order, "spendableAfterTransfers": balance}
                for balance, order in states.values()
            ],
            "protectedRecoveryExcluded": True,
            "optionalReserveIsFiniteRewardStock": account["optionalReserve"],
            "status": "candidate financial prefix only; assumes spatial predicates and actor availability succeed",
            "afterFundingSelections": after_funding,
            "mainAffordableSelectionCount": sum(row["mainAffordable"] for row in after_funding),
            "allOptionalTasksAffordableAfterFundingCount": sum(
                row["allOptionalTasksAffordable"] is True for row in after_funding
            ),
        }
    return {**projection, "optionalPrefixAnalysisByDifficulty": output}


def _check_safe_balance(balance, label):
    if not isinstance(balance, dict) or set(balance) != set(RESOURCES):
        raise ValueError(f"{label} has an invalid resource vector")
    for resource, value in balance.items():
        if type(value) is not int or value < 0 or value > MAX_SAFE_INTEGER:
            raise ValueError(f"{label} overflows safe integer {resource}")


def _check_safe_states(states, label):
    for balance, _order in states.values():
        _check_safe_balance(balance, label)


def project_batch(requests, *, root=ROOT):
    """Validate and project a single batch; attach optional-state analysis."""
    bun = shutil.which("bun")
    if not bun:
        raise RuntimeError("Bun is required for fulfillment-dossier projection; validation was not skipped")
    if not BRIDGE.is_file():
        raise RuntimeError(f"Fulfillment projector bridge is missing: {BRIDGE}")
    payload = {"requests": requests}
    try:
        result = subprocess.run(
            [bun, "run", str(BRIDGE)],
            input=json.dumps(payload, ensure_ascii=False, separators=(",", ":")),
            text=True,
            capture_output=True,
            check=False,
            cwd=root,
        )
    except OSError as error:
        raise RuntimeError(f"Could not start Bun fulfillment projector: {error}") from error
    if result.returncode:
        raise RuntimeError(
            "Fulfillment projection failed; validation was not skipped: "
            + (result.stderr.strip() or f"bridge exit {result.returncode}")
        )
    try:
        decoded = json.loads(result.stdout)
    except json.JSONDecodeError as error:
        raise RuntimeError(f"Fulfillment projector returned malformed JSON: {error}") from error
    if not isinstance(decoded, dict) or not isinstance(decoded.get("projections"), list):
        raise RuntimeError("Fulfillment projector returned an invalid response envelope")
    if len(decoded["projections"]) != len(requests):
        raise RuntimeError("Fulfillment projector response count does not match request count")
    for projection, request in zip(decoded["projections"], requests):
        if projection.get("episodeId") != request.get("episodeId"):
            raise RuntimeError("Fulfillment projector changed batch order or episode identity")
        projection.update(
            _with_optional_analysis(projection, request["accountsByDifficulty"])
        )
    return decoded


if __name__ == "__main__":
    try:
        request = json.load(sys.stdin)
        if not isinstance(request, dict) or not isinstance(request.get("requests"), list):
            raise ValueError("stdin must contain {\"requests\":[ProjectionRequest,...]}")
        result = project_batch(request["requests"])
        sys.stdout.write(json.dumps(result, ensure_ascii=False, separators=(",", ":")) + "\n")
    except Exception as error:
        sys.stderr.write(f"fulfillment-dossier helper failed: {error}\n")
        sys.exit(1)
