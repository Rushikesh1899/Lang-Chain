from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int


new_person: Person = {
    "name": "Rushikesh",
    "age": 28
}

print(new_person)