from fastapi.testclient import TestClient
from app.main import app
client=TestClient(app)
def test_onboarding_capability():
    r=client.post("/tenants",json={"tenant_id":"tenant-a"})
    assert r.status_code==200
    assert "roles" in r.json()
def test_missing_tenant_fails_closed():
    assert client.post("/tenants",json={"tenant_id":""}).status_code==422
