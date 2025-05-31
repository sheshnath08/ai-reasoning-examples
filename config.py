import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Model configurations
DEFAULT_LLM_MODEL = os.getenv("MODEL_NAME", "gpt-4o")
