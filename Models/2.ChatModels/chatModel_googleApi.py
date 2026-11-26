from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import  load_dotenv

load_dotenv()

googleMode = ChatGoogleGenerativeAI(model = "gemini-1.5-pro")

result = googleMode.invoke("What is the capital of india?")

print(result)