import re
from utils.llm_helpers import call_openai

problem = "What is the sum of the first 100 natural numbers?"
response = call_openai(f"Write Python code to solve this: {problem}")

# Extract code block from response
code_match = re.search(r"```python(.*?)```", response, re.DOTALL)
if code_match:
    code = code_match.group(1).strip()
else:
    # fallback: assume whole response is code (not recommended for general use)
    code = response.strip()

print("Generated code:\n", code)

# Execute the extracted code
exec(code)
