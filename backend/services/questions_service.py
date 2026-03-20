from typing import List
from backend.models.schemas import QuestionCreate, QuestionOut

# Placeholder questions service

class QuestionsService:
    def list_questions(self) -> List[QuestionOut]:
        return [QuestionOut(id=1, subject="Math", topic="Algebra", content="1+1=?", answer="2")]

    def get_question(self, question_id: int) -> QuestionOut:
        return QuestionOut(id=question_id, subject="Math", topic="Algebra", content="1+1=?", answer="2")

    def create_question(self, data: QuestionCreate) -> QuestionOut:
        return QuestionOut(id=2, **data.dict())
