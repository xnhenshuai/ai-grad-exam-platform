from fastapi import APIRouter, HTTPException
from typing import List
from backend.models.schemas import QuestionCreate, QuestionOut
from backend.services.questions_service import QuestionsService

router = APIRouter()
service = QuestionsService()


@router.get("/", response_model=List[QuestionOut])
def list_questions():
    return service.list_questions()


@router.get("/{question_id}", response_model=QuestionOut)
def get_question(question_id: int):
    return service.get_question(question_id)


@router.post("/", response_model=QuestionOut)
def create_question(payload: QuestionCreate):
    return service.create_question(payload)
