from app.schemas.student_schema import StudentCreate, StudentUpdate
from sqlalchemy.orm import Session
from app.models.student import Student
from sqlalchemy.exc import IntegrityError

def get_students(db: Session):
    return db.query(Student).all()


def get_student(db: Session, student_id: int):
    return db.query(Student).filter(Student.id == student_id).first()

def create_student(db: Session, student_data: StudentCreate):
    student = Student(
        name=student_data.name,
        email=student_data.email
    )

    try:
        db.add(student)
        db.commit()
        db.refresh(student)

        return student

    except IntegrityError:
        db.rollback()
        raise

def update_student(
    db: Session,
    student_id: int,
    student_data: StudentUpdate
):
    student = (
        db.query(Student)
        .filter(Student.id == student_id)
        .first()
    )

    if student is None:
        return None

    student.name = student_data.name
    student.email = student_data.email

    try:
        db.commit()
        db.refresh(student)

        return student

    except IntegrityError:
        db.rollback()
        raise

def delete_student(db: Session, student_id: int):
    student = (
        db.query(Student)
        .filter(Student.id == student_id)
        .first()
    )

    if student is None:
        return None

    try:
        db.delete(student)
        db.commit()

        return student

    except Exception:
        db.rollback()
        raise

def get_student_by_email(db: Session, email: str):
    return db.query(Student).filter(Student.email == email).first()
