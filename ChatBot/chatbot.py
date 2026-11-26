from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-5.5")

chatHistory = [
    SystemMessage(content="You are a helpful AI assistant")
]

while True:
    userInput = input("You: ")
    #we save the history so that chatbot can rembember the previous discussion
    chatHistory.append(HumanMessage(content=userInput))
    if userInput == "exit":
        break
    result  = model.invoke(chatHistory)
    chatHistory.append(AIMessage(content=result.content))
    print("AI: ",result.content)

print(chatHistory)