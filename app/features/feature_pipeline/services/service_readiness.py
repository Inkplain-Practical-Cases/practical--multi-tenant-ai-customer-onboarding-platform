# Check deployment readiness: isolated onboarding service.
def service_readiness(s: dict) -> dict:
    # Gate readiness on tenant-matched provisioning and defined role policy.
    s["ready"]=s["provisioning"]["tenant_id"]==s["tenant_id"] and "tenant_admin" in s["roles"]
    return s
