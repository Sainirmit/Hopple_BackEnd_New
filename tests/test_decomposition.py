# tests/test_decomposition.py
from hopple_core import HoppleCore

def test_decompose_task():
    core = HoppleCore()
    subtasks = core.decompose_task("Test task")
    assert isinstance(subtasks, list), "Subtasks should be a list"
    # Expect at least two subtasks now due to our simulation
    assert len(subtasks) >= 2, "Expected at least two subtasks"
    assert "subtask generated dynamically" in subtasks[1], "Simulated subtask missing"
