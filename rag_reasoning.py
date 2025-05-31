from utils.llm_helpers import call_with_context, load_custom_documents

context = load_custom_documents()
query = "Explain the idea behind Tree-of-Thought prompting."
answer = call_with_context(query, context)
print(answer)