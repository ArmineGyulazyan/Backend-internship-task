from fastapi import APIRouter, Depends
from typing import List, Dict
from controllers import PostController, TokenController
from Models import Post, User


route = APIRouter()

@route.post('/create_post', response_model=None, status_code=201, dependencies=[Depends(TokenController.get_current_user)])
async def create_post(post:Post, user:User=Depends(TokenController.get_current_user)):
    await PostController.create_post(post)


@route.get('/posts', response_model=List[Post], status_code=201, dependencies=[Depends(TokenController.get_current_user)])
async def read_posts(user:User=Depends(TokenController.get_current_user)):
    db_posts = await PostController.get_posts()
    return await db_posts.to_list(length=None)


@route.put('/update_post/{post_id}', response_model=None, status_code=200, dependencies=[Depends(TokenController.get_current_user)])
async def update_post(post_id:int, new_args:Dict=None,user:User=Depends(TokenController.get_current_user)):
    await PostController.update_post(post_id, new_args)


@route.delete('/delete_post/{post_id}', response_model=None, status_code=204, dependencies=[Depends(TokenController.get_current_user)])
async def delete_post(post_id:int,user:User=Depends(TokenController.get_current_user)):
    await PostController.delete_post(post_id)