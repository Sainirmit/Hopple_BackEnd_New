# tests/test_server.py
from fastapi.testclient import TestClient
from server import app

client = TestClient(app)

def test_process_endpoint():
    response = client.get("/process/?task=Plan%20a%20product%20launch")
    # Check for HTTP 200 OK
    assert response.status_code == 200, "Expected status code 200"
    
    # Parse the JSON response
    json_data = response.json()
    
    # Verify that the response is a dictionary with a key 'plan'
    assert isinstance(json_data, dict), "Response should be a dictionary"
    assert "plan" in json_data, "Response should contain key 'plan'"
    
    plan = json_data["plan"]
    # For recognized tasks, we expect plan to be a dictionary with the expected keys
    assert isinstance(plan, dict), "Plan should be a dictionary for recognized tasks"
    for key in ["tasks", "assignments", "meeting_summary"]:
        assert key in plan, f"Plan should contain key '{key}'"

def test_process_endpoint_generic():
    response = client.get("/process/?task=Some%20random%20task")
    # Check for HTTP 200 OK
    assert response.status_code == 200, "Expected status code 200"
    
    # Parse the JSON response
    json_data = response.json()
    
    # Verify that the response is a dictionary with a key 'plan'
    assert isinstance(json_data, dict), "Response should be a dictionary"
    assert "plan" in json_data, "Response should contain key 'plan'"
    
    plan = json_data["plan"]
    # For unrecognized tasks, our design returns a string error message
    if isinstance(plan, dict):
        # If by chance it's a dictionary, then check it has the expected keys
        for key in ["tasks", "assignments", "meeting_summary"]:
            assert key in plan, f"Plan should contain key '{key}'"
    else:
        # Otherwise, check that the string contains an error message
        assert "not recognized" in plan.lower(), "Expected error message for unrecognized task"
