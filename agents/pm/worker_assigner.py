# agents/pm/worker_assigner.py
from utils.logger import log_debug

def assign_workers(tasks: list, workers: list) -> list:
    log_debug("Assigning tasks to workers.")
    assignments = []
    num_workers = len(workers)
    for idx, task in enumerate(tasks):
        worker = workers[idx % num_workers]
        assignment = {"task": task["task"], "worker": worker, "priority": task["priority"]}
        assignments.append(assignment)
    log_debug(f"Assignments: {assignments}")
    return assignments
