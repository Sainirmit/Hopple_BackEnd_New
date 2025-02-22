# # agents/pm_agent.py
# import asyncio
# from utils.async_utils import async_call_mistral
# from utils.logger import log_info, log_debug, log_error

# class ProjectManagementAgent:
#     def __init__(self):
#         log_info("ProjectManagementAgent initialized.")
#         # Simulated list of workers. In a production system, this might come from a database.
#         self.workers = ["Alice", "Bob", "Charlie", "Dana"]
#         self.sub_agents = {}  # To keep track of dynamically created sub-agents

#     async def generate_plan(self, goal: str):
#         """
#         Generate a project plan using asynchronous AI calls and dynamic sub-agent creation.
#         """
#         log_info(f"Generating plan for goal: {goal}")
#         tasks = await self.create_tasks(goal)
        
#         # Decide if a sub-agent is needed (for project management tasks)
#         if "project" in goal.lower() or "plan" in goal.lower():
#             # Dynamically import and create a Task Assignment sub-agent
#             from agents.task_assignment_agent import TaskAssignmentAgent
#             task_agent = TaskAssignmentAgent(tasks)
#             self.sub_agents["task_assignment"] = task_agent
            
#             # Run the sub-agent asynchronously and get processed tasks
#             processed_tasks = await task_agent.run(goal)
            
#             # After processing, put the sub-agent to sleep
#             await task_agent.sleep()
            
#             # Simulate immediate approval, then terminate the sub-agent
#             await task_agent.terminate()
            
#             # Use the processed tasks from the sub-agent
#             tasks = processed_tasks

#         # Continue with priority assignment, worker assignment, and meeting summarization
#         prioritized_tasks = self.assign_priorities(tasks)
#         assignments = self.assign_workers(prioritized_tasks)
#         meeting_summary = await self.summarize_meetings(goal)
#         plan = {
#             "tasks": prioritized_tasks,
#             "assignments": assignments,
#             "meeting_summary": meeting_summary
#         }
#         log_info("Plan generated successfully.")
#         return plan

#     async def create_tasks(self, goal: str):
#         """
#         Asynchronously generate tasks using AI with contextual prompting and apply hybrid rule-based adjustments.
#         """
#         log_debug("Creating tasks for the goal.")
#         context = "User: Acme Corp. Team with agile workflow. "
        
#         if "product launch" in goal.lower():
#             prompt = (
#                 f"{context}Generate a list of tasks for planning a product launch. "
#                 "List each task on a new line."
#             )
#         else:
#             prompt = (
#                 f"{context}Generate a list of generic project management tasks. "
#                 "List each task on a new line."
#             )
#         ai_output = await async_call_mistral(prompt)
#         if ai_output:
#             tasks = [
#                 {"task": task.strip(), "priority": None}
#                 for task in ai_output.split("\n") if task.strip()
#             ]
#         else:
#             # Fallback hardcoded tasks
#             if "product launch" in goal.lower():
#                 tasks = [
#                     {"task": "Define product features and unique selling points", "priority": None},
#                     {"task": "Identify target audience and market segments", "priority": None},
#                     {"task": "Develop marketing strategy and content plan", "priority": None},
#                     {"task": "Set timeline for pre-launch, launch, and post-launch activities", "priority": None},
#                     {"task": "Establish KPIs and success metrics", "priority": None}
#                 ]
#             else:
#                 tasks = [
#                     {"task": "Define goals and objectives", "priority": None},
#                     {"task": "Break down tasks into manageable steps", "priority": None},
#                     {"task": "Assign responsibilities", "priority": None},
#                     {"task": "Set deadlines and milestones", "priority": None}
#                 ]
#         # Hybrid rule-based adjustment: flag tasks that are too short
#         for task in tasks:
#             if len(task["task"]) < 15:
#                 task["task"] += " (review needed)"
        
#         log_debug(f"Created tasks: {tasks}")
#         return tasks

#     async def summarize_meetings(self, goal: str):
#         """
#         Asynchronously summarize meetings using AI.
#         """
#         log_debug("Summarizing meetings for the goal.")
#         context = "User: Acme Corp. Team with agile workflow. "
#         if "product launch" in goal.lower():
#             prompt = (
#                 f"{context}Summarize a meeting about planning a product launch strategy, highlighting key milestones."
#             )
#         else:
#             prompt = (
#                 f"{context}Summarize a generic project meeting, highlighting key decisions and next steps."
#             )
#         ai_summary = await async_call_mistral(prompt)
#         if ai_summary:
#             summary = ai_summary
#         else:
#             if "product launch" in goal.lower():
#                 summary = "Meeting summary: Discussed product launch strategy and identified key milestones."
#             else:
#                 summary = "Meeting summary: No meeting data available."
#         log_debug(f"Meeting summary: {summary}")
#         return summary

#     def assign_priorities(self, tasks):
#         """
#         Assign priorities to tasks.
#         TODO: In the future, integrate AI-driven dynamic prioritization or more advanced rule-based logic.
#         Currently, we assign based on task order.
#         """
#         log_debug("Assigning priorities to tasks.")
#         for i, task in enumerate(tasks):
#             if i == 0:
#                 task["priority"] = "High"
#             elif i == 1:
#                 task["priority"] = "Medium"
#             else:
#                 task["priority"] = "Low"
#         log_debug(f"Tasks after priority assignment: {tasks}")
#         return tasks

#     def assign_workers(self, tasks):
#         """
#         Assign tasks to available workers.
#         TODO: In production, integrate with a company HR database or employee management system for dynamic worker assignment.
#         Here, we cycle through a predefined list of workers.
#         """
#         log_debug("Assigning tasks to workers.")
#         assignments = []
#         num_workers = len(self.workers)
#         for idx, task in enumerate(tasks):
#             worker = self.workers[idx % num_workers]
#             assignment = {"task": task["task"], "worker": worker, "priority": task["priority"]}
#             assignments.append(assignment)
#         log_debug(f"Assignments: {assignments}")
#         return assignments

# agents/pm_agent.py
import asyncio
from utils.async_utils import async_call_mistral
from utils.logger import log_info, log_debug, log_error
from agents.pm.task_creator import create_tasks
from agents.pm.meeting_summarizer import summarize_meetings
from agents.pm.priority_assigner import assign_priorities
from agents.pm.worker_assigner import assign_workers

class ProjectManagementAgent:
    def __init__(self):
        log_info("ProjectManagementAgent initialized.")
        self.workers = ["Alice", "Bob", "Charlie", "Dana"]
        self.sub_agents = {}  # To keep track of dynamically created sub-agents

    async def generate_plan(self, goal: str):
        log_info(f"Generating plan for goal: {goal}")
        tasks = await create_tasks(goal)
        
        if "project" in goal.lower() or "plan" in goal.lower():
            from agents.task_assignment_agent import TaskAssignmentAgent
            task_agent = TaskAssignmentAgent(tasks)
            self.sub_agents["task_assignment"] = task_agent
            processed_tasks = await task_agent.run(goal)
            await task_agent.sleep()
            await task_agent.terminate()
            tasks = processed_tasks

        prioritized_tasks = assign_priorities(tasks)
        assignments = assign_workers(prioritized_tasks, self.workers)
        meeting_summary = await summarize_meetings(goal)
        plan = {
            "tasks": prioritized_tasks,
            "assignments": assignments,
            "meeting_summary": meeting_summary
        }
        log_info("Plan generated successfully.")
        return plan
