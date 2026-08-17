import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "backend"))

from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)

def test_get_students():
    response = client.get("/students/")

    assert response.status_code == 200

def test_get_student(test_student):
    response = client.get(f"/students/{test_student.id}")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == test_student.id
    assert data["name"] == "Arjun"
    assert data["email"] == "arjun@example.com"

def test_get_student_not_found():
    response = client.get("/students/9999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Student not found"

def test_create_student():
    response = client.post(
        "/students/",
        json={
            "name": "Test Student",
            "email": "teststudent@example.com"
        }
    )

    assert response.status_code == 201

    data = response.json()

    assert data["name"] == "Test Student"
    assert data["email"] == "teststudent@example.com"
    assert "id" in data