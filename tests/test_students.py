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

def test_create_student_duplicate_email(test_student):
    response = client.post(
        "/students/",
        json={
            "name": "Duplicate Student",
            "email": test_student.email
        }
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Email already exists"

def test_create_student_invalid_email():
    response = client.post(
        "/students/",
        json={
            "name": "Invalid Email",
            "email": "invalid-email"
        }
    )

    assert response.status_code == 422

def test_create_student_empty_name():
    response = client.post(
        "/students/",
        json={
            "name": "",
            "email": "emptyname@example.com"
        }
    )

    assert response.status_code == 422

def test_create_student_whitespace_name():
    response = client.post(
        "/students/",
        json={
            "name": "   ",
            "email": "whitespace@example.com"
        }
    )

    assert response.status_code == 422

def test_create_student_name_too_long():
    response = client.post(
        "/students/",
        json={
            "name": "A" * 101,
            "email": "toolong@example.com"
        }
    )

    assert response.status_code == 422

def test_update_student(test_student):
    response = client.put(
        f"/students/{test_student.id}",
        json={
            "name": "Arjun Updated",
            "email": "arjun_updated@example.com"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == test_student.id
    assert data["name"] == "Arjun Updated"
    assert data["email"] == "arjun_updated@example.com"

def test_update_student_not_found():
    response = client.put(
        "/students/9999",
        json={
            "name": "Nobody",
            "email": "nobody@example.com"
        }
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Student not found"

def test_update_student_duplicate_email(test_student):
    db_student = test_student

    second_student_response = client.post(
        "/students/",
        json={
            "name": "Second Student",
            "email": "second@example.com"
        }
    )

    assert second_student_response.status_code == 201

    second_student = second_student_response.json()

    response = client.put(
        f"/students/{second_student['id']}",
        json={
            "name": "Second Student",
            "email": db_student.email
        }
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Email already exists"

def test_delete_student(test_student):
    response = client.delete(
        f"/students/{test_student.id}"
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == test_student.id
    assert data["name"] == "Arjun"
    assert data["email"] == "arjun@example.com"

def test_delete_student_not_found():
    response = client.delete("/students/9999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Student not found"