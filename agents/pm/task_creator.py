# agents/pm/task_creator.py
from utils.async_utils import async_call_mistral
from utils.logger import log_debug

async def create_tasks(goal: str) -> list:
    log_debug("Creating tasks for the goal.")
    context = "User: Acme Corp. Team with agile workflow. "
    if "product launch" in goal.lower():
        prompt = (
            f"{context}Generate a list of tasks for planning a product launch. "
            "List each task on a new line."
        )
    else:
        prompt = (
            f"{context}Generate a list of generic project management tasks. "
            "List each task on a new line."
        )
    ai_output = await async_call_mistral(prompt)
    if ai_output:
        tasks = [{"task": task.strip(), "priority": None} for task in ai_output.split("\n") if task.strip()]
    else:
        if "product launch" in goal.lower():
            tasks = [
                {"task": "Define product features and unique selling points", "priority": None},
                {"task": "Identify target audience and market segments", "priority": None},
                {"task": "Develop marketing strategy and content plan", "priority": None},
                {"task": "Set timeline for pre-launch, launch, and post-launch activities", "priority": None},
                {"task": "Establish KPIs and success metrics", "priority": None}
            ]
        else:
            tasks = [
                {"task": "Define goals and objectives", "priority": None},
                {"task": "Break down tasks into manageable steps", "priority": None},
                {"task": "Assign responsibilities", "priority": None},
                {"task": "Set deadlines and milestones", "priority": None}
            ]
    # Hybrid rule-based adjustment: flag tasks that are too short.
    for task in tasks:
        if len(task["task"]) < 15:
            task["task"] += " (review needed)"
    log_debug(f"Created tasks: {tasks}")
    return tasks
