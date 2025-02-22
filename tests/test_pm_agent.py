# tests/test_pm_agent.py
import asyncio
from agents.pm.priority_assigner import assign_priorities
from agents.pm_agent import ProjectManagementAgent

def test_generate_plan_for_launch():
    agent = ProjectManagementAgent()
    plan = asyncio.run(agent.generate_plan("Plan a product launch"))
    # Verify that the plan is a dictionary and has expected keys
    assert isinstance(plan, dict), "Plan should be a dictionary"
    for key in ["tasks", "assignments", "meeting_summary"]:
        assert key in plan, f"Plan should contain key '{key}'"

def test_generate_plan_generic():
    agent = ProjectManagementAgent()
    plan = asyncio.run(agent.generate_plan("Some random task"))
    # Verify that a generic plan is returned as a dictionary
    assert isinstance(plan, dict), "Plan should be a dictionary"
    for key in ["tasks", "assignments", "meeting_summary"]:
        assert key in plan, f"Plan should contain key '{key}'"
