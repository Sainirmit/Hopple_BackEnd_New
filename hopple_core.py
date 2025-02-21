# # hopple_core.py

# class HoppleCore:
#     def __init__(self):
#         # Future: Initialize structures for sub-agents, context, etc.
#         print("HoppleCore initialized!")
#         # Any additional initialization code

#     def process_task(self, task: str):
#         """
#         Process a high-level task by decomposing it and invoking sub-agents.
#         For now, it delegates project management tasks to the PM sub-agent.
#         """
#         # For simplicity, if the task mentions 'project' or 'plan', use the PM sub-agent.
#         if "project" in task.lower() or "plan" in task.lower():
#             from agents.pm_agent import ProjectManagementAgent
#             pm_agent = ProjectManagementAgent()
#             return pm_agent.generate_plan(task)
#         else:
#             return f"Task '{task}' is not recognized yet."

# hopple_core.py
from utils.logger import log_info, log_debug, log_error

class HoppleCore:
    def __init__(self):
        log_info("HoppleCore initialized.")

    def process_task(self, task: str):
        log_info(f"Processing task: {task}")
        try:
            if "project" in task.lower() or "plan" in task.lower():
                from agents.pm_agent import ProjectManagementAgent
                pm_agent = ProjectManagementAgent()
                result = pm_agent.generate_plan(task)
                log_info("Task processed by PM sub-agent.")
                return result
            else:
                log_debug(f"Task '{task}' is not recognized.")
                return f"Task '{task}' is not recognized yet."
        except Exception as e:
            log_error(f"Error processing task '{task}': {e}")
            return f"Error: {e}"
