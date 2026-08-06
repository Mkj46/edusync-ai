from fastapi import APIRouter
from app.services import student_service
from app.schemas.student_schema import Student, StudentCreate
from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.database import get_db

router = APIRouter()


@router.get("/", response_model=list[Student])
def get_students(
    db: Session = Depends(get_db)
):
    return student_service.get_students(db)


@router.get("/{student_id}", response_model=Student)
def get_student(student_id: int):
    return student_service.get_student(student_id)


@router.post("/", response_model=Student, status_code=201)
def create_student(student: StudentCreate):
    return student_service.create_student(student)