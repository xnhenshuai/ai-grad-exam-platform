from datetime import datetime
from backend.models.schemas import StudyPlanCreate, StudyPlanOut

# Placeholder study plan service

class StudyPlanService:
    def get_study_plan(self, user_id: int) -> StudyPlanOut:
        return StudyPlanOut(id=1, user_id=user_id, plan_name="Starter Plan", details="Review algebra daily", updated_at=datetime.utcnow())

    def refresh_study_plan(self, user_id: int) -> StudyPlanOut:
        return StudyPlanOut(id=1, user_id=user_id, plan_name="Updated Plan", details="Focus on weaknesses", updated_at=datetime.utcnow())
