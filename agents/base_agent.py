# agents/base_agent.py
from utils.logger import log_info, log_debug

class BaseAgent:
    def __init__(self, name: str):
        self.name = name
        self.status = "active"  # possible statuses: active, sleeping, terminated
        log_info(f"{self.name} initialized and active.")

    async def run(self, task: str):
        """
        Run the sub-agent's task.
        Must be implemented by the subclass.
        """
        raise NotImplementedError("Subclasses must implement this method.")

    async def sleep(self):
        """
        Put the sub-agent into sleep (hibernation) mode.
        """
        self.status = "sleeping"
        log_info(f"{self.name} is now in sleep mode.")

    async def terminate(self):
        """
        Terminate the sub-agent.
        """
        self.status = "terminated"
        log_info(f"{self.name} has been terminated.")
