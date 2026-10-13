# Application entry point: builds the FastAPI app and mounts the feature router.
from fastapi import FastAPI
from app.features.feature_pipeline.router import router
app = FastAPI(title="Tenant registry and scoped API")
app.include_router(router)

# Audit is an independent, source-backed persistence concern.
from app.core.request_audit_middleware import RequestAuditMiddleware
app.add_middleware(RequestAuditMiddleware)
