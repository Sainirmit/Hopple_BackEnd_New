# hopple_core.py
from utils.logger import log_info, log_debug, log_error

class HoppleCore:
    def __init__(self):
        log_info("HoppleCore initialized.")

    async def process_task(self, task: str):
        log_info(f"Processing task: {task}")
        try:
            # Placeholder: Future dynamic task decomposition can be integrated here
            decomposed_tasks = self.decompose_task(task)
            log_debug(f"Decomposed tasks: {decomposed_tasks}")

            # For now, if the task is about project management, delegate to the PM sub-agent.
            if "project" in task.lower() or "plan" in task.lower():
                from agents.pm_agent import ProjectManagementAgent
                pm_agent = ProjectManagementAgent()
                # Await the async generate_plan method
                result = await pm_agent.generate_plan(task)
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
        In the future, this will use an AI model (e.g., Mistral via Ollama) to break down the task.
        For now, it returns a list containing the original task and a simulated sub-task.
        """
        log_info(f"Decomposing task: {task}")
        # TODO: Replace the following simulated decomposition with a call to Mistral
        simulated_subtasks = [task, f"{task} - subtask generated dynamically"]
        log_debug(f"Simulated subtasks: {simulated_subtasks}")
        return simulated_subtasks
