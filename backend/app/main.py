from core.database import create_db_and_tables
from fastapi import FastAPI
from api import user, admin, subscription
from models.models import User, Subscription, Service, Payment

app = FastAPI()
app.include_router(user.router)
app.include_router(admin.router)
app.include_router(subscription.router)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/")
async def root():
    return {"Hello": "World"}