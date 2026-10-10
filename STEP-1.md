# STEP-1 of 6 — Tenant registry and scoped API

## What you build
A working HTTP boundary that rejects malformed data and returns a tenant-scoped accepted response.

## What you learn
Thin routing doors, Pydantic validation, handler orchestration, service isolation and pytest contract tests.

## Run
```bash
python -m pip install -r requirements.txt
python -m pytest -q
uvicorn app.main:app --reload
```

## Verify
POST `/tenants` with JSON containing non-empty `tenant_id` and `tenant_id`; expect HTTP 200. Empty fields produce 422.

## Next
STEP-2 adds the next enterprise capability without breaking this contract.
