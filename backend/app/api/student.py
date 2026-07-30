from fastapi import APIRouter

router = APIRouter()


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


@router.get("/")
def get_students():
    return students

@router.get("/{student_id}")
def get_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return student

    return {
        "message": "Student not found"
    }