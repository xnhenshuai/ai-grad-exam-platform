from fastapi import APIRouter
from typing import List
from backend.models.schemas import MistakeCreate, MistakeOut
from backend.services.mistakes_service import MistakesService

router = APIRouter()
service = MistakesService()


@router.get("/", response_model=List[MistakeOut])
def list_mistakes(user_id: int = 1):
    return service.list_mistakes(user_id)


@router.post("/", response_model=MistakeOut)
def create_mistake(payload: MistakeCreate):
    return service.create_mistake(payload)


@router.put("/{mistake_id}", response_model=MistakeOut)
def update_mistake(mistake_id: int, note: str):
    return service.update_mistake(mistake_id, note)
