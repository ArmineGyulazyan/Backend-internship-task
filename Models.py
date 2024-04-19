from pydantic import BaseModel


class User(BaseModel):
    user_id:int
    user_mail:str
    password:str


class Post(BaseModel):
    post_id:int
    title:str
    post_content:str
    owner:User


class Token(BaseModel):
    token_val:str
    token_type:str