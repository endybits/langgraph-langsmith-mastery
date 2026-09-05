"""
This script loads environment variables from a .env file and prints the value of LANGCHAIN_TRACING_V2.
"""

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

# Initialize the chat model
llm = ChatOpenAI(model="gpt-5.6-luna")

# Invoke the model with prompt
response = llm.invoke("¿Hola, cómo estás?")
print(response.content)
