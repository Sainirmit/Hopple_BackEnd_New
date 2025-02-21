# tests/test_server.py
from fastapi.testclient import TestClient
from server import app

client = TestClient(app)

def test_process_endpoint():
    response = client.get("/process/?task=Plan%20a%20product%20launch")
    assert response.status_code == 200
    json_data = response.json()
    assert "plan" in json_data
    assert isinstance(json_data["plan"], list)
    # Optionally, check that the plan has a minimum expected number of tasks
    assert len(json_data["plan"]) >= 4
