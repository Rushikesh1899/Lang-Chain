from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="maxwell-model/Maxwell-V1-Flash",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN"),
    task="text-generation"
)

modelVal = ChatHuggingFace(llm=llm)

modelVal.invoke("What is the capital of india?")