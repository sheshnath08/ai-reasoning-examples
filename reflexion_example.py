from utils.llm_helpers import call_openai

question = "What is 23 * 7? Show your steps."
initial = call_openai(question)
critique = call_openai(f"Please review the following answer and suggest improvements:\n{initial}")
revision = call_openai(f"Revise the answer below using the critique:\nAnswer: {initial}\nCritique: {critique}")

print("Refined Answer:\n", revision)