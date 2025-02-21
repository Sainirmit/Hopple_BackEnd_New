# import openai
# from duckduckgo_search import ddg

# class ResearchAgent:
#     def __init__(self, openai_api_key, search_api_key=None):
#         self.openai_api_key = openai_api_key

#     def web_search(self, query):
#         results = ddg(query, max_results=5)
#         return "\n".join([f"{r['title']}: {r['href']}" for r in results])

#     def summarize(self, text):
#         response = openai.ChatCompletion.create(
#             model="gpt-4",
#             messages=[{"role": "system", "content": "Summarize this info:"},
#                       {"role": "user", "content": text}],
#         )
#         return response["choices"][0]["message"]["content"]

#     def run(self, query):
#         print(f"🔎 Searching the web for: {query}")
#         search_results = self.web_search(query)
#         summary = self.summarize(search_results)
#         return summary
