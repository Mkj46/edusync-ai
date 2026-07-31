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


def get_students():
    return students


def get_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return student

    return None