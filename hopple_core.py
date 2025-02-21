# hopple_core.py

class HoppleCore:
    def __init__(self):
        # Future: Initialize structures for sub-agents, context, etc.
        print("HoppleCore initialized!")


def process_task(self, task: str):
        """
        Process a high-level task by decomposing it and invoking sub-agents.
        """
        print(f"Processing task: {task}")
        if "project" in task.lower() or "plan" in task.lower():
            from pm_agent import ProjectManagementAgent
            pm_agent = ProjectManagementAgent()
            plan = pm_agent.generate_plan(task)
            print("Generated plan:", plan)
            return plan
        else:
            return f"Task '{task}' is not recognized yet."