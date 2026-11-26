from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage

chatTemplate = ChatPromptTemplate([
    ("system", "You are helful {domain} expert"),
    ("human", "Explain in simple terms, what is {topic}")
])

prompt = chatTemplate.invoke({"domain": "Cricket", "topic": "Dusra"})

print(prompt)