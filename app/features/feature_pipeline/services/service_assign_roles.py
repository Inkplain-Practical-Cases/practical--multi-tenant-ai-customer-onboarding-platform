# Assign scoped tenant roles: isolated onboarding service.
def service_assign_roles(s: dict) -> dict:
    # Default-closed role map for one isolated tenant.
    s["roles"]={"tenant_admin":["read","configure"],"tenant_viewer":["read"]}
    return s
