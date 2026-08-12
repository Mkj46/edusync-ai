from pydantic import BaseModel


class StudentCreate(BaseModel):
    name: str
    email: str

class StudentUpdate(BaseModel):
    name: str
    email: str

class Student(BaseModel):
    id: int
    name: str
    email: str