from fastapi import FastAPI, status, Body, HTTPException, Path
from pydantic import BaseModel
from typing import List, Annotated

app = FastAPI()
users = []

valid_username = Annotated[str, Path(min_length=3, max_length=20, description="Enter a name", example="Max")]
valid_age = Annotated[int, Path(ge=18, le=100, description="Enter age", example=19)]
valid_id = Annotated[int, Path(ge=0, le=10000000, description="Enter id", example=2)]


class User(BaseModel):
    id: valid_id
    username: valid_username
    age: valid_id

@app.get("/users")
async def get_user() -> List[User]:
    return users

@app.post('/user/{username}/{age}')
async def create_user(username: valid_username, age: valid_age) -> str:
    try:
        id = users[-1].id + 1
    except:
        id = 1

    user = User(id=id, username=username, age=age)
    users.append(user)
    return user

@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: valid_id, username: valid_username, age: valid_age) -> str:
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user

    raise HTTPException(status_code=404, detail="User was not found" )

@app.delete('/user/{user_id}')
async def del_user(user_id: valid_id) -> str:
    for __id, user in enumerate(users):
        if user.id == user_id:
            users.pop(__id)
            return user
    raise HTTPException(status_code=404, detail="User was not found")





