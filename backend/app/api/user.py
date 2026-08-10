from fastapi import APIRouter

router = APIRouter()

@router.get("/users/me")
async def get_current_user():
    return {"user": "current_user"}