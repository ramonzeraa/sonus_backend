from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

def init_llm():
    load_dotenv()
    chave_api = os.getenv("API_KEY")
    return ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest", api_key=chave_api)

llm = init_llm()

def generateQuestion(content):
    message = HumanMessage(content=f"Crie uma questão para ensino fundamental com o conteúdo de {content}.")
    resposta = llm.invoke([message])
    
    return resposta.content
