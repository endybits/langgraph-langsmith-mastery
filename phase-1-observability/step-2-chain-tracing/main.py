"""LangChain  Expresion Language (LCEL)"""
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(model="gpt-5.6-luna")

user_input = str(input("Ingresa un mensaje:\n"))
nombre = "Endy"

prompt = ChatPromptTemplate.from_template("Responde a {name}, quien te escribió:\n{input}")

chain = prompt | llm | StrOutputParser()
resp = chain.invoke({"input": user_input, "name": nombre})
print(resp)
