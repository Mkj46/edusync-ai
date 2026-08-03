from fastapi import HTTPException
from app.repositories import student_repository
from app.schemas.student_schema import StudentCreate


def get_students():
    return student_repository.get_students()


def get_student(student_id: int):
    student = student_repository.get_student(student_id)

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student


def create_student(student: StudentCreate):
    existing_student = student_repository.get_student_by_email(student.email)

    if existing_student:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    return student_repository.create_student(student)