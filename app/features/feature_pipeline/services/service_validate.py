# Business service: normalizes an accepted tenant-scoped request.
def service_validate(payload: dict) -> dict:
    # Never silently accept an empty tenant, even if invoked outside HTTP.
    if not payload.get("tenant_id", "").strip():
        raise ValueError("tenant_id required")
    return {"status": "accepted", "tenant_id": payload["tenant_id"], "tenant_id": payload["tenant_id"]}
