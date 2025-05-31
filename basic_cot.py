from utils.llm_helpers import call_openai

prompt = "Q: If there are 3 apples and you buy 2 more, how many do you have? Let's think step by step."
response = call_openai(prompt)
print(response)