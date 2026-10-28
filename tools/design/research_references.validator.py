"""Validate downloaded research provenance and bytes without approving reuse."""

import hashlib
import json


def audit_references(root, manifest):
    errors = []
    root = root.resolve()
    seen = set()
    for asset in manifest["assets"]:
        identity = asset["id"]
        if identity in seen:
            errors.append(f"Duplicate research reference: {identity}")
        seen.add(identity)
        path = (root / asset["path"]).resolve()
        if not path.is_relative_to(root):
            errors.append(f"Unsafe reference path: {identity}")
            continue
        if not path.is_file():
            errors.append(f"Missing reference: {identity}")
            continue
        content = path.read_bytes()
        if len(content) != asset["bytes"]:
            errors.append(f"Reference size drift: {identity}")
        if hashlib.sha256(content).hexdigest() != asset["sha256"]:
            errors.append(f"Reference hash drift: {identity}")
        if not all(asset.get(field) for field in ("license", "author", "sourcePage")):
            errors.append(f"Missing rights: {identity}")
        if asset.get("productionApproved") is not False:
            errors.append(f"Research photo falsely approved: {identity}")
        if path.suffix.lower() in (".jpg", ".jpeg") and not content.startswith(
            b"\xff\xd8\xff"
        ):
            errors.append(f"Invalid JPEG reference: {identity}")
        if path.suffix.lower() in (".json", ".geojson"):
            try:
                json.loads(content)
            except (ValueError, UnicodeDecodeError):
                errors.append(f"Invalid JSON reference: {identity}")
    return errors
