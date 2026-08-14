from fastapi import HTTPException
from app.repositories import student_repository
from app.schemas.student_schema import StudentCreate, StudentUpdate
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

def get_students(db: Session):
    return student_repository.get_students(db)


def get_student(db: Session, student_id: int):
    student = student_repository.get_student(db, student_id)

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student  


def create_student(db: Session, student: StudentCreate):
    existing_student = student_repository.get_student_by_email(db,student.email)
    if existing_student:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    try:
        return student_repository.create_student(db, student)

    except IntegrityError:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

def update_student(
    db: Session,
    student_id: int,
    student_data: StudentUpdate
):
    try:
        student = student_repository.update_student(
            db,
            student_id,
            student_data
        )

    except IntegrityError:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student

def delete_student(db: Session, student_id: int):
    student = student_repository.delete_student(db, student_id)

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student