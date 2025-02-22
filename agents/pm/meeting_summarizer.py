# agents/pm/meeting_summarizer.py
from utils.async_utils import async_call_mistral
from utils.logger import log_debug

async def summarize_meetings(goal: str) -> str:
    log_debug("Summarizing meetings for the goal.")
    context = "User: Acme Corp. Team with agile workflow. "
    if "product launch" in goal.lower():
        prompt = (
            f"{context}Summarize a meeting about planning a product launch strategy, highlighting key milestones."
        )
    else:
        prompt = (
            f"{context}Summarize a generic project meeting, highlighting key decisions and next steps."
        )
    ai_summary = await async_call_mistral(prompt)
    if ai_summary:
        summary = ai_summary
    else:
        summary = ("Meeting summary: Discussed product launch strategy and identified key milestones."
                   if "product launch" in goal.lower() else "Meeting summary: No meeting data available.")
    log_debug(f"Meeting summary: {summary}")
    return summary
