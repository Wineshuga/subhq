from fastapi import APIRouter
from seeds import users
from schemas.schema import UserPublic, UserCreate, SubscriptionCreate, ServiceCreate, PaymentCreate

router = APIRouter()

@router.get("/users")
async def get_users(user: UserPublic):
    print(f'Users from db: {user}')
    return {"users": users}

@router.get("/users/{user_id}")
async def get_user(user: UserPublic, user_id: int):
    user = next((u for u in users if u["id"] == user_id), None)
    return {"user": user}
