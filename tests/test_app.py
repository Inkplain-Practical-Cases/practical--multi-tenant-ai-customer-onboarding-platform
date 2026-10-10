# Tenant-scoped request contract regressions.
from fastapi.testclient import TestClient
from app.main import app
client=TestClient(app)
def test_valid_tenant():
    r=client.post('/tenants',json={'tenant_id':'tenant-a'})
    assert r.status_code==200
    assert r.json()['tenant_id']=='tenant-a'
def test_invalid_tenant():
    assert client.post('/tenants',json={'tenant_id':''}).status_code==422
