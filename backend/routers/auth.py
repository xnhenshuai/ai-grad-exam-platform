from fastapi import APIRouter, HTTPException
from backend.models.schemas import UserCreate, UserOut
from backend.services.auth_service import AuthService

router = APIRouter()
service = AuthService()


@router.post("/register", response_model=UserOut)
def register(user: UserCreate):
    return service.register_user(user.username, user.password)


@router.post("/login")
def login(user: UserCreate):
    auth = service.authenticate_user(user.username, user.password)
    if not auth:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"access_token": "fake-token", "token_type": "bearer"}


@router.get("/me", response_model=UserOut)
def me(token: str = "fake-token"):
    return service.get_current_user(token)
