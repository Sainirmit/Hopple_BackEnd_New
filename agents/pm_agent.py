# # pm_agent.py
# from utils.logger import log_info

# class ProjectManagementAgent:
#     def __init__(self):
#         # Initialize any PM-specific variables here if needed
#         log_info("ProjectManagementAgent initialized.")
#         pass

#     def generate_plan(self, goal: str):
#         log_info(f"Generating plan for goal: {goal}")
#         """
#         Given a high-level project management goal, generate a simple plan.
#         Currently hardcoded for MVP demonstration.
#         """
#         if "product launch" in goal.lower():
#             plan = [
#                 "Define product features and unique selling points.",
#                 "Identify target audience and market segments.",
#                 "Develop marketing strategy and content plan.",
#                 "Set timeline for pre-launch, launch, and post-launch activities.",
#                 "Establish KPIs and success metrics."
#             ]
#         else:
#             plan = [
#                 "Define goals and objectives.",
#                 "Break down tasks into manageable steps.",
#                 "Assign responsibilities.",
#                 "Set deadlines and milestones."
#             ]
#         log_info("Plan generated successfully.")    
#         return plan

# agents/pm_agent.py
from utils.logger import log_info, log_debug, log_error

class ProjectManagementAgent:
    def __init__(self):
        log_info("ProjectManagementAgent initialized.")
        # Simulated list of workers. In a production system, this might come from a database.
        self.workers = ["Alice", "Bob", "Charlie", "Dana"]

    def generate_plan(self, goal: str):
        """
        Generate a project plan based on a high-level goal.
        Combines task creation, priority assignment, worker assignment, and meeting summarization.
        """
        log_info(f"Generating plan for goal: {goal}")
        tasks = self.create_tasks(goal)
        prioritized_tasks = self.assign_priorities(tasks)
        assignments = self.assign_workers(prioritized_tasks)
        meeting_summary = self.summarize_meetings(goal)
        plan = {
            "tasks": prioritized_tasks,
            "assignments": assignments,
            "meeting_summary": meeting_summary
        }
        log_info("Plan generated successfully.")
        return plan

    def create_tasks(self, goal: str):
        """
        Create a list of tasks based on the goal.
        TODO: Integrate with AI (e.g., using Mistral) to dynamically generate tasks.
        For now, we return hardcoded tasks.
        """
        log_debug("Creating tasks for the goal.")
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
        log_debug(f"Created tasks: {tasks}")
        return tasks

    def assign_priorities(self, tasks):
        """
        Assign priorities to tasks.
        TODO: Use dynamic or AI-driven methods for assigning priorities.
        Currently, we assign based on task order.
        """
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

    def assign_workers(self, tasks):
        """
        Assign tasks to available workers.
        TODO: In a real scenario, integrate with an HR or task management system.
        Here, we simply cycle through a predefined list of workers.
        """
        log_debug("Assigning tasks to workers.")
        assignments = []
        num_workers = len(self.workers)
        for idx, task in enumerate(tasks):
            worker = self.workers[idx % num_workers]
            assignment = {"task": task["task"], "worker": worker, "priority": task["priority"]}
            assignments.append(assignment)
        log_debug(f"Assignments: {assignments}")
        return assignments

    def summarize_meetings(self, goal: str):
        """
        Summarize meetings related to the given goal.
        TODO: Integrate with an AI summarization tool (like Mistral).
        For now, return a placeholder summary.
        """
        log_debug("Summarizing meetings for the goal.")
        if "product launch" in goal.lower():
            summary = "Meeting summary: Discussed product launch strategy and identified key milestones."
        else:
            summary = "Meeting summary: No meeting data available."
        log_debug(f"Meeting summary: {summary}")
        return summary
    