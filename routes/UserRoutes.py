from fastapi import APIRouter
from typing import List, Dict
from controllers import UserController
from Models import User


route = APIRouter()

@route.post('/create_user', response_model=None, status_code=201)
async def create_user(user:User):
    await UserController.create_user(user)


@route.get('/users', response_model=List[User], status_code=201)
async def read_users():
    db_users = await UserController.get_users()
    return await db_users.to_list(length=None)


@route.put('/update_user/{user_id}', response_model=None, status_code=200)
async def update_user(user_id:int, new_args:Dict=None):
    await UserController.update_user(user_id, new_args)


@route.delete('/delete_user/{user_id}', response_model=None, status_code=204)
async def delete_user(user_id:int):
    await UserController.delete_user(user_id)