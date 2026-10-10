# Emit tenant-scoped audit trail: isolated onboarding service.
def service_audit(s: dict) -> dict:
    # Record outcome, not credentials or customer secrets.
    s["audit"]={"tenant_id":s["tenant_id"],"ready":s["ready"],"event":"onboarding_checked"}
    return s
