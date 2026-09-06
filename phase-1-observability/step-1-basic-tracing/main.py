"""
This script runs a llm invocation to test the first time
of LS tracing with a simple unique run.
"""

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

# Initialize the chat model
llm = ChatOpenAI(model="gpt-5.6-luna")

# Invoke the model with prompt
response = llm.invoke("¿Hola, cómo estás?")
print(response.content)
