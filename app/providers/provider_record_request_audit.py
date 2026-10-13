"""Persist redacted tenant API request audit events in SQLite, without request bodies."""
import os
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4

def provider_record_request_audit(method: str, route: str, status: int, duration_ms: float, database_path: str | None = None) -> str:
    """Write one API request and one linked outcome event with foreign keys enabled."""
    path = database_path or os.getenv("INKPLAIN_AUDIT_DB", "data/tenant_audit.sqlite3")
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    identity = uuid4().hex
    created_at = datetime.now(timezone.utc).isoformat()
    with sqlite3.connect(path) as connection:
        connection.execute("PRAGMA foreign_keys = ON")
        connection.execute("""CREATE TABLE IF NOT EXISTS tenant_api_requests (
            id TEXT PRIMARY KEY,
            route TEXT NOT NULL,
            method TEXT NOT NULL,
            created_at TEXT NOT NULL
        )""")
        connection.execute("""CREATE TABLE IF NOT EXISTS tenant_api_events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            request_id TEXT NOT NULL REFERENCES tenant_api_requests(id),
            http_status INTEGER NOT NULL,
            duration_ms REAL NOT NULL,
            occurred_at TEXT NOT NULL
        )""")
        connection.execute("INSERT INTO tenant_api_requests (id, route, method, created_at) VALUES (?, ?, ?, ?)", (identity, route, method, created_at))
        connection.execute("INSERT INTO tenant_api_events (request_id, http_status, duration_ms, occurred_at) VALUES (?, ?, ?, ?)",
                           (identity, int(status), round(duration_ms, 2), created_at))
    return identity
