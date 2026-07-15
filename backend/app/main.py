from fastapi import FastAPI
from api import user, admin, subscription

app = FastAPI()
app.include_router(user.router)
app.include_router(admin.router)
app.include_router(subscription.router)

@app.get("/")
async def root():
    return {"Hello": "World"}