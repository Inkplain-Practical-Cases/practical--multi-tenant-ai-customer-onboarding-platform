# Tenant model: validates non-empty client tenant identity.
from pydantic import BaseModel, Field
class TenantRequest(BaseModel):
    tenant_id: str = Field(min_length=1)
