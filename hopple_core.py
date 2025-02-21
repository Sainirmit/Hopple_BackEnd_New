# hopple_core.py
from utils.logger import log_info, log_debug, log_error

class HoppleCore:
    def __init__(self):
        log_info("HoppleCore initialized.")

    def process_task(self, task: str):
        log_info(f"Processing task: {task}")
        try:
            # Placeholder: Future dynamic task decomposition can be integrated here
            decomposed_tasks = self.decompose_task(task)
            log_debug(f"Decomposed tasks: {decomposed_tasks}")

            # For now, if the task is about project management, delegate to the PM sub-agent.
            if "project" in task.lower() or "plan" in task.lower():
                from agents.pm_agent import ProjectManagementAgent
                pm_agent = ProjectManagementAgent()
                result = pm_agent.generate_plan(task)
                log_info("Task processed by PM sub-agent successfully.")
                return result
            else:
                log_debug(f"Task '{task}' is not recognized. No sub-agent available.")
                return f"Task '{task}' is not recognized yet."
        except Exception as e:
            log_error(f"Error processing task '{task}': {e}")
            return f"Error: {e}"

    def decompose_task(self, task: str):
        """
        Placeholder for dynamic task decomposition.
        In the future, this will use an LLM or a more sophisticated algorithm to break down the task.
        For now, it simply returns the original task in a list.
        """
        log_info(f"Decomposing task: {task}")
        # TODO: Implement dynamic decomposition logic
        return [task]
