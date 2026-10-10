# Application validation: reject empty scoped tenant identifiers.
def service_validate(payload: dict) -> dict:
    tenant_id=payload.get('tenant_id','').strip()
    if not tenant_id:
        raise ValueError('tenant_id required')
    return {'status':'accepted','tenant_id':tenant_id}
