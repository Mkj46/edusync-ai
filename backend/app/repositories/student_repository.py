from app.schemas.student_schema import StudentCreate
from sqlalchemy.orm import Session
from app.models.student import Student
students = [
    {
        "id": 1,
        "name": "Madhav",
        "email": "madhav@example.com"
    },
    {
        "id": 2,
        "name": "Rahul",
        "email": "rahul@example.com"
    }
]


def get_students(db: Session):
    return db.query(Student).all()


def get_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return student

    return None
def create_student(student: StudentCreate):
    new_student = {
        "id": len(students) + 1,
        "name": student.name,
        "email": student.email
    }

    students.append(new_student)

    return new_student
def get_student_by_email(email: str):
    for student in students:
        if student["email"] == email:
            return student

    return None 
