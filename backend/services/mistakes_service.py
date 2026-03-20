from typing import List
from backend.models.schemas import MistakeCreate, MistakeOut
from datetime import datetime

# Placeholder mistakes service

class MistakesService:
    def list_mistakes(self, user_id: int) -> List[MistakeOut]:
        return [MistakeOut(id=1, user_id=user_id, question_id=1, note="Need review", created_at=datetime.utcnow())]

    def create_mistake(self, data: MistakeCreate) -> MistakeOut:
        return MistakeOut(id=2, created_at=datetime.utcnow(), **data.dict())

    def update_mistake(self, mistake_id: int, note: str) -> MistakeOut:
        return MistakeOut(id=mistake_id, user_id=1, question_id=1, note=note, created_at=datetime.utcnow())
