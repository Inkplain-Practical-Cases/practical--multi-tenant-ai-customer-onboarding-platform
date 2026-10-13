"""Assert recorded tenant requests and outcomes have a valid FK, no request payload."""
import sqlite3
from app.providers.provider_record_request_audit import provider_record_request_audit

def test_relational_api_audit(tmp_path):
    path = str(tmp_path / "audit.sqlite3")
    identifier = provider_record_request_audit("POST", "/api", 200, 9.2, path)
    with sqlite3.connect(path) as conn:
        assert conn.execute("SELECT COUNT(*) FROM tenant_api_requests WHERE id=?", (identifier,)).fetchone()[0] == 1
        assert conn.execute("SELECT COUNT(*) FROM tenant_api_events WHERE request_id=?", (identifier,)).fetchone()[0] == 1
        assert conn.execute("PRAGMA foreign_key_check").fetchall() == []
