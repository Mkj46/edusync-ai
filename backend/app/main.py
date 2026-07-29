from fastapi import FastAPI

app = FastAPI(
    title="EduSync AI API",
    version="1.0.0"
)

@app.get("/")
def root():
    print("Root function executed")

    return {
        "message": "Welcome to EduSync AI"
    }