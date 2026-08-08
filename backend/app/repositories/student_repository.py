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
def create_student(db: Session, student_data: StudentCreate):
    student = Student(
        name=student_data.name,
        email=student_data.email
    )

    db.add(student)
    db.commit()
    db.refresh(student)

    return student

def get_student_by_email(db: Session, email: str):
    return db.query(Student).filter(Student.email == email).first()
