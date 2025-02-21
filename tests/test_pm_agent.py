# tests/test_pm_agent.py
from agents.pm_agent import ProjectManagementAgent

def test_generate_plan_for_launch():
    agent = ProjectManagementAgent()
    plan = agent.generate_plan("Plan a product launch")
    # Verify that the plan is a list and has expected steps
    assert isinstance(plan, list)
    assert len(plan) >= 5  # We expect at least 5 tasks for a product launch

def test_generate_plan_generic():
    agent = ProjectManagementAgent()
    plan = agent.generate_plan("Some random task")
    # Verify that a generic plan is returned
    assert isinstance(plan, list)
    assert len(plan) >= 4  # Expect a fallback generic plan with multiple steps
