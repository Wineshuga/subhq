from fastapi import APIRouter
from seeds import users

router = APIRouter()

@router.get("/users")
async def get_users():
    return {"users": users}

@router.get("/users/{user_id}")
async def get_user(user_id: int):
    user = next((u for u in users if u["id"] == user_id), None)
    return {"user": user}
