from fastapi import FastAPI
from typing import List
from models import User
from uuid import UUID, uuid4
from models import Role, Gender


app = FastAPI()

db: List[User] = [
    
    User(
        id=uuid4(),
        first_name="Barzan",
        last_name="Saeedpour",
        middle_name="h",
        gender = Gender.male,
        roles = [Role.admin],
        ),
    
    User(
        id=uuid4(),
        first_name="parsa",
        last_name="soli",
        middle_name="h",
        gender = Gender.male,
        roles = [Role.student, Role.user],
        ),
]

@app.get('/')
async def root():
    return {"Hello": "world!"}


@app.get('/api/v1/users')
async def fetch_users():
    return db;