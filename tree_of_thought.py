from utils.llm_helpers import call_openai, evaluate_paths

prompt = "What are some ways to make 24 using 6, 6, and 6?"
paths = [call_openai(prompt + f"\nPath {i+1}:") for i in range(3)]

for i, p in enumerate(paths):
    print(f"Path {i+1}:\n{p}\n")

best = evaluate_paths(paths)
print("Best path selected:\n", best)