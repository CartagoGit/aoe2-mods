"""Strict numeric primitives shared by authored design and finite analysis."""

RESOURCES = ('food', 'wood', 'gold', 'stone')


def is_positive_integer(value):
    return type(value) is int and value > 0


def resource_amounts(value):
    if not isinstance(value, dict) or set(value) - set(RESOURCES):
        raise ValueError("Unknown resource or invalid resource vector")
    if any(type(amount) is not int or amount < 0 for amount in value.values()):
        raise ValueError("Resource amounts must be nonnegative integers")
    return {key: value.get(key, 0) for key in RESOURCES}


def audit_count_thresholds(episode):
    """Reject malformed thresholds before dependent comparisons or ledger audits."""
    thresholds = []
    counted_kinds = {
        "entity-state", "current-entity-presence", "checkpoint-entity-presence",
        "area-state", "transport-journey", "paired-delivery", "finite-wave-resolution",
    }
    for objective in episode["objectivePlan"]:
        context = f"{episode['id']}/{objective['id']}"
        for requirement in objective["predicate"]["requirements"]:
            for field in ('requiredCount', 'distinctDestinationCount', 'minimumPerDestination'):
                if field in requirement or (field == 'requiredCount' and requirement['kind'] in counted_kinds):
                    thresholds.append((
                        f"{context}/{requirement['id']}: counter",
                        requirement.get(field),
                    ))
        for ledger in objective["predicate"].get("exportedLedgers", []):
            thresholds.append((
                f"{context}/{ledger['id']}: ledger minimum",
                ledger.get("minimumCount"),
            ))
    for position, group in enumerate(episode["worldContract"].get("survivorGroups", [])):
        thresholds.append((
            f"{episode['id']}/survivor-{position}: survival threshold",
            group.get("minimumAliveOrAlreadySafe"),
        ))
    return [
        f"{context} must be a positive integer"
        for context, value in thresholds
        if not is_positive_integer(value)
    ]


def audit_payment_vectors(episode):
    failures = []
    for objective in episode['objectivePlan']:
        if 'resourceAmounts' in objective['predicate']:
            try:
                resource_amounts(objective['predicate']['resourceAmounts'])
            except ValueError as error:
                failures.append(f"{episode['id']}/{objective['id']}: {error}")
        for requirement in objective['predicate']['requirements']:
            context = f"{episode['id']}/{objective['id']}/{requirement['id']}"
            vectors = []
            if 'amounts' in requirement or requirement['kind'] == 'resource-transaction':
                vectors.append(requirement.get('amounts'))
            if requirement['kind'] == 'resource-transaction':
                allocations = requirement.get('allocations')
                if not isinstance(allocations, dict):
                    failures.append(f'{context}: invalid payment allocations')
                else:
                    vectors.extend(allocations.values())
            vectors.extend(receipt.get('amounts')
                           for receipt in requirement.get('requiredPaymentReceipts', []))
            for vector in vectors:
                try:
                    resource_amounts(vector)
                except ValueError as error:
                    failures.append(f'{context}: {error}')
    return failures


def audit_objective_numbers(scenario):
    return audit_count_thresholds(scenario) + audit_payment_vectors(scenario)
