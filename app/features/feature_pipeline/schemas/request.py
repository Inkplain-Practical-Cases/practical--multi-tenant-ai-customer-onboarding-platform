# Input contract: Pydantic validates fields at the external boundary.
from pydantic import BaseModel, Field
class TenantRequest(BaseModel):
    tenant_id: str = Field(min_length=1)
    tenant_id: str = Field(min_length=1)
