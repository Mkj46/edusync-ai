from fastapi import FastAPI
from app.api.student import router as student_router
from app.db.database import engine
from sqlalchemy import text

app = FastAPI(
    title="EduSync AI API",
    version="1.0.0"
)

@app.on_event("startup")
def test_database_connection():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        print("✅ Database connected successfully!")
    except Exception as e:
        print("❌ Database connection failed!")
        print(e)

app.include_router(student_router, prefix="/students", tags=["Students"])


@app.get("/")
def root():
    return {
        "message": "Welcome to EduSync AI"
    }