from fastapi import FastAPI
from backend.routers import auth, questions, mistakes, study_plan


def include_routes(app: FastAPI):
    app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
    app.include_router(questions.router, prefix="/api/questions", tags=["questions"])
    app.include_router(mistakes.router, prefix="/api/mistakes", tags=["mistakes"])
    app.include_router(study_plan.router, prefix="/api/study-plan", tags=["study_plan"])
