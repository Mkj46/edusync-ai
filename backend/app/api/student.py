from fastapi import APIRouter
from app.services import student_service
from app.schemas.student_schema import Student

router = APIRouter()


@router.get("/", response_model=list[Student])
def get_students():
    return student_service.get_students()


@router.get("/{student_id}", response_model=Student)
def get_student(student_id: int):
    return student_service.get_student(student_id)