from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()
users = {'1': 'Имя: Example, возраст: 18'}

valid_username = Annotated[str, Path(min_length=3, max_length=20, description="Enter a name", example="Max")]
valid_age = Annotated[int, Path(ge=18, le=100, description="Enter age", example=19)]
valid_id = Annotated[int, Path(ge=0, le=10000000, description="Enter id", example=2)]


@app.get("/users")
async def get_message() -> dict:
    return users


@app.post('/user/{username}/{age}')
async def create_message (username: valid_username, age: valid_age) -> str:
    user_id = str(int (max(users,key=int)) + 1)
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} is registered"

@app.put("/user/{user_id}/{username}/{age}")
async def update_message(user_id: valid_id, username: valid_username, age: valid_age) -> str:
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} is registered"

@app.delete('/user/{user_id}')
async def update_message(user_id: valid_id) -> str:
    users.pop(str(user_id))
    return f"User {user_id} has been deleted"


