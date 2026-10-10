# Provision scoped resources: isolated onboarding service.
def service_provision(s: dict) -> dict:
    # Deterministic local stand-in for an external provisioning adapter.
    s["provisioning"]={"tenant_id":s["tenant_id"],"status":"ready","resource_count":2}
    return s
