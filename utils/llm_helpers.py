import openai
from config import OPENAI_API_KEY, DEFAULT_LLM_MODEL

# Set up the OpenAI client
client = openai.OpenAI(api_key=OPENAI_API_KEY)


def call_openai(prompt, model=DEFAULT_LLM_MODEL, temperature=0.7):
    """
    Sends a prompt to the OpenAI Chat Completions API using v1 SDK.
    """
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=temperature
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error calling OpenAI: {e}"


def evaluate_paths(paths, model=DEFAULT_LLM_MODEL):
    """
    Evaluates a list of reasoning paths and selects the best one using the LLM.
    """
    prompt = "Evaluate the following options and determine which one is the best and why:\n\n"
    for i, path in enumerate(paths):
        prompt += f"Option {i + 1}:\n{path}\n\n"
    prompt += "Select the best option and explain your choice."

    try:
        return call_openai(prompt, model=model, temperature=0.3)
    except Exception as e:
        return f"Error during path evaluation: {e}"


def call_with_context(query, context, model=DEFAULT_LLM_MODEL, temperature=0.3):
    """
    Answers a user query using the given context.
    """
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "Use the provided context to answer the user's question."},
                {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {query}"}
            ],
            temperature=temperature
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error calling OpenAI with context: {e}"


def load_custom_documents():
    """
    Loads predefined custom documents.
    """
    return [
        "Tree-of-Thought prompting involves decomposing a complex problem into intermediate reasoning steps.",
        "Chain-of-Thought is a prompting technique where the model is encouraged to explain its reasoning step-by-step.",
        "Self-Consistency involves sampling multiple reasoning paths and selecting the most common or coherent answer."
    ]
