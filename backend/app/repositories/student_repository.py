from app.schemas.student_schema import StudentCreate
from sqlalchemy.orm import Session
from app.models.student import Student

def get_students(db: Session):
    return db.query(Student).all()


def get_student(db: Session, student_id: int):
    return db.query(Student).filter(Student.id == student_id).first()

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
