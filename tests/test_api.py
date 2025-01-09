from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_sustainable_alternatives():
    response = client.post("/sustainable-manufacturing", json={
        "description": "Smartphone case made of plastic"
    })
    assert response.status_code == 200
    data = response.json()
    assert "materials" in data
    assert "process" in data
    assert "vendors" in data
    assert "shipping" in data
