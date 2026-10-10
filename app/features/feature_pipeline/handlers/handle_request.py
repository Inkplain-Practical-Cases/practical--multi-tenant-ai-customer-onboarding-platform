# Thin orchestrator of scoped onboarding operations.
from app.features.feature_pipeline.schemas.request import TenantRequest
from app.features.feature_pipeline.services.service_validate import service_validate
from app.features.feature_pipeline.services.service_configure import service_configure
from app.features.feature_pipeline.services.service_assign_roles import service_assign_roles
def handle_request(body: TenantRequest) -> dict:
    state=service_validate(body.model_dump())
    state=service_configure(state)
    state=service_assign_roles(state)
    return state
