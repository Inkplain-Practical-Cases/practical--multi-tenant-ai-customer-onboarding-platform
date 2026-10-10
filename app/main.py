# Application entry point: builds the FastAPI app and mounts the feature router.
from fastapi import FastAPI
from app.features.feature_pipeline.router import router
app = FastAPI(title="Tenant registry and scoped API")
app.include_router(router)
