# tests/test_server.py
from fastapi.testclient import TestClient
from server import app

client = TestClient(app)

def test_process_endpoint():
    response = client.get("/process/?task=Plan%20a%20product%20launch")
    assert response.status_code == 200, "Expected status code 200"
    json_data = response.json()
    
    # Verify that the response is a dictionary and contains the 'plan' key.
    assert isinstance(json_data, dict), "Response should be a dictionary"
    assert "plan" in json_data, "Response JSON should contain a 'plan' key"
    
    plan = json_data["plan"]
    # Verify the plan has the expected structure.
    assert isinstance(plan, dict), "Plan should be a dictionary"
    assert "tasks" in plan, "Plan should have 'tasks'"
    assert "assignments" in plan, "Plan should have 'assignments'"
    assert "meeting_summary" in plan, "Plan should have 'meeting_summary'"
