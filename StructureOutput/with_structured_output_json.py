
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal
from pydantic import BaseModel, Field

load_dotenv()

model = ChatOpenAI(model = "gpt-5.5")

#schema with json
json_schema = {
    "title": "Review",
    "type": "object",
    "properties": {
        "type": "array",
        "items": {
            "type": "string"
        },
        "description": "Write down all the key themes disscused in the review in a list"
    }
}


structureModel = model.with_structured_output(json_schema)

result = structureModel.invoke("A literature  review  is a  surveys  scholarly  articles, books  and  other  sources  relevant  to  a particular issue,  area  of  research,  or  theory,  and  by  so  doing, providing  a  description,  summary,  and  critical evaluation of these works. Literature reviews are designed to provide an overview of sources you have explored while researching a particular topic and to demonstrate to your readers how your research fits into  the  larger  field  of  study  (libguides.usc.edu,  n.d.). ")

print(result)
# print(result["summary"])
# print(result["name"])