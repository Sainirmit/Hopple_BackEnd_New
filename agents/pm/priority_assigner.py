# agents/pm/priority_assigner.py
from utils.logger import log_debug

def assign_priorities(tasks: list) -> list:
    log_debug("Assigning priorities to tasks.")
    for i, task in enumerate(tasks):
        if i == 0:
            task["priority"] = "High"
        elif i == 1:
            task["priority"] = "Medium"
        else:
            task["priority"] = "Low"
    log_debug(f"Tasks after priority assignment: {tasks}")
    return tasks