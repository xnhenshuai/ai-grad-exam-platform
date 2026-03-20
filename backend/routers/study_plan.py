from fastapi import APIRouter
from backend.models.schemas import StudyPlanOut
from backend.services.study_plan_service import StudyPlanService

router = APIRouter()
service = StudyPlanService()


@router.get("/", response_model=StudyPlanOut)
def get_study_plan(user_id: int = 1):
    return service.get_study_plan(user_id)


@router.post("/refresh", response_model=StudyPlanOut)
def refresh_study_plan(user_id: int = 1):
    return service.refresh_study_plan(user_id)
