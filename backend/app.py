from fastapi import FastAPI
from backend.api.routes import include_routes

app = FastAPI(title="AI Grad Exam Platform Backend")

include_routes(app)

@app.get("/health")
def health_check():
    return {"status": "ok"}
