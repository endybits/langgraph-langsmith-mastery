"""
This script loads environment variables from a .env file and prints the value of LANGCHAIN_TRACING_V2.
"""

import os
from dotenv import load_dotenv

load_dotenv()

print("Environment variables loaded successfully.")
print(f"LANGCHAIN_TRACING_V2: {os.getenv('LANGCHAIN_TRACING_V2')}")
