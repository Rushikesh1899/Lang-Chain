from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# chatMode = ChatOpenAI(model="gpt-5.5")

# result = chatMode.invoke("Which mountain is large in the world?")
# print(result.content)

# we applying temprature on this which is why we can get more presice output

# chatMode = ChatOpenAI(model="gpt-5.5", temperature=0)

# result = chatMode.invoke("Suggest me 5 indian male names")
# print(result.content)

# chatMode = ChatOpenAI(model="gpt-5.5", temperature=1.8)

# result = chatMode.invoke("Write a 5 line poem on cricket")
# print(result.content)

# now we see max completion tokens which is why we gets only that much tokens in return

chatMode = ChatOpenAI(model="gpt-5.5", temperature=1.8, max_completion_tokens=20)

result = chatMode.invoke("Write a 5 line poem on cricket")
print(result.content)