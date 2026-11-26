from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

result =  client.chat.completions.create(
    model = "gpt-5.6-terra",
    messages = [{"role": "user", "content" : "What is the capital of india?"}]
)

print(result)


