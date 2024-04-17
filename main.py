from fastapi import FastAPI, HTTPException
from typing import List
from models import User
from uuid import UUID, uuid4
from models import Role, Gender


app = FastAPI()

db: List[User] = [

    User(
        # id=uuid4(),
        id=UUID("e1270928-f047-4380-a329-c490ea2b1580"),
        first_name="Barzan",
        last_name="Saeedpour",
        middle_name="h",
        gender=Gender.male,
        roles=[Role.admin],
    ),

    User(
        id=UUID("ab2b2bd8-9890-4337-afd4-9007f7f5ec43"),
        first_name="parsa",
        last_name="soli",
        middle_name=None,
        gender=Gender.male,
        roles=[Role.student, Role.user],
    ),
]


@app.get('/')
async def root():
    return {"Hello": "world!"}

@app.get('/api/v1/users')
async def fetch_users():
    return db

@app.post('/api/v1/users')
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}

@app.delete('/api/v1/users/{user_id}')
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return {"id": user.id}
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exists."
    )
        