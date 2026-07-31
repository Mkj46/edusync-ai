from fastapi import HTTPException
from app.repositories import student_repository


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