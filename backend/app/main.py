from fastapi import FastAPI
from app.api.student import router as student_router

app = FastAPI(
    title="EduSync AI API",
    version="1.0.0"
)

app.include_router(student_router, prefix="/students", tags=["Students"])


@app.get("/")
def root():
    return {
        "message": "Welcome to EduSync AI"
    }