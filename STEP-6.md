# STEP-6 — Emit tenant-scoped audit trail

Use `pytest -q`; read this step's source and CRD to follow tenant-scoped execution.


## Database (Entity) Relations
SQLite writes accepted HTTP request metadata and linked outcome events. No request body is stored. See STEP-6.erd and the STEP-6-ERD Simulator tab.
