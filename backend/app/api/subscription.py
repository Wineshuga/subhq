from fastapi import APIRouter
from seeds import subscriptions

router = APIRouter()

@router.get("/user/{user_id}/subscriptions")
async def get_user_subscriptions(user_id: int):
  user_subscriptions = [sub for sub in subscriptions if sub["userId"] == user_id]
  return {"subscriptions": user_subscriptions}

@router.get("/subscription/{subscription_id}")
async def get_subscription(subscription_id: int):
  subscription = next((sub for sub in subscriptions if sub["id"] == subscription_id), None)
  return {"subscription": subscription}