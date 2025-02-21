# import argparse
# import json
# from agents.research_agent import ResearchAgent

# # Load API keys
# with open("config.json") as f:
#     config = json.load(f)

# # CLI Parser
# parser = argparse.ArgumentParser(description="Hopple - AI Agents CLI")
# parser.add_argument("task", type=str, help="Task name (e.g., 'research')")
# parser.add_argument("query", type=str, nargs="?", help="Query for the agent")

# args = parser.parse_args()

# # Execute the selected agent
# if args.task == "research":
#     agent = ResearchAgent(config["openai_api_key"], config["serpapi_key"])
#     result = agent.run(args.query)
#     print("\n🔍 Research Results:\n", result)
# else:
#     print("❌ Invalid task. Available: research")
