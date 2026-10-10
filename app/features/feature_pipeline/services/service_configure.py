# Validate customer configuration: isolated onboarding service.
def service_configure(s: dict) -> dict:
    # Keep onboarding defaults explicit and independently testable.
    s["config"]={"region":"eu-central-1","max_users":25,"tenant_id":s["tenant_id"]}
    return s
