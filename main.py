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
        gender = Gender.male,
        roles = [Role.admin],
        ),
    
    User(
        id=uuid4(),
        first_name="parsa",
        last_name="soli",
        gender = Gender.male,
        roles = [Role.student, Role.user],
        ),
]

@app.get('/')
def root():
    return {"Hello": "world!"}