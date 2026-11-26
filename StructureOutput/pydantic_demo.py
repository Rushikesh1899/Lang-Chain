from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str = "Rushi"
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0, lt=10, default=5, description="A decimal value representing the cgpa of student")


new_stud = {"name": "Sagar" , "age": "28", "email": "abc12@gmail.com"}

stud = Student(**new_stud)

# print(dict(stud)["name"])
# print(list(stud))
print(stud.model_dump())