from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal

load_dotenv()

model = ChatOpenAI(model = "gpt-5.5")

# here we create schema 
class Review(TypedDict):
    title: str
    key_themes: Annotated[list[str], "Write down all the key themes discussed in the review in a list"]
    pros: Annotated[Optional[list[str]], "Write down all the pros inside a list"]
    cons: Annotated[Optional[list[str]], "Write down all the cons inside a list"]
    name: Annotated[Optional[str], "Write the name of the reviewer"]
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Literal["Pos", "Neg"]

structureModel = model.with_structured_output(Review)

result = structureModel.invoke("A literature  review  is a  surveys  scholarly  articles, books  and  other  sources  relevant  to  a particular issue,  area  of  research,  or  theory,  and  by  so  doing, providing  a  description,  summary,  and  critical evaluation of these works. Literature reviews are designed to provide an overview of sources you have explored while researching a particular topic and to demonstrate to your readers how your research fits into  the  larger  field  of  study  (libguides.usc.edu,  n.d.). ")

print(result)
# print(result["summary"])
print(result["name"])