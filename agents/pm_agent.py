# pm_agent.py

class ProjectManagementAgent:
    def __init__(self):
        # Initialize any PM-specific variables here if needed
        pass

    def generate_plan(self, goal: str):
        """
        Given a high-level project management goal, generate a simple plan.
        Currently hardcoded for MVP demonstration.
        """
        if "product launch" in goal.lower():
            plan = [
                "Define product features and unique selling points.",
                "Identify target audience and market segments.",
                "Develop marketing strategy and content plan.",
                "Set timeline for pre-launch, launch, and post-launch activities.",
                "Establish KPIs and success metrics."
            ]
        else:
            plan = [
                "Define goals and objectives.",
                "Break down tasks into manageable steps.",
                "Assign responsibilities.",
                "Set deadlines and milestones."
            ]
        return plan
