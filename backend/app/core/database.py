from dotenv import load_dotenv
from sqlmodel import SQLModel, create_engine, Session
import os

load_dotenv()

database_url = os.getenv("DB_URL")
engine = create_engine(database_url, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
