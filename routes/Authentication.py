from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from jose import JWTError, jwt
from Models import User, Token
from controllers import UserController, TokenController
from Services import Tokens

route = APIRouter()


@route.post('/register', response_model=None, status_code=201)
async def register(user:User):
    await UserController.create_user(user)


@route.post('/login', response_model=None, status_code=201)
async def login(data:OAuth2PasswordRequestForm=Depends()):
    user = await TokenController.authenticate_user(data.username, data.password)
    if not user:
        raise HTTPException(status_code=401)
    access_token = TokenController.create_access_token(data={'sub':user['user_mail']})
    login_token = Token(token_val=access_token, token_type="bearer")
    await Tokens.insert_one(login_token.dict())


@route.post('/logout', response_model=None, status_code=201)
async def logout(token:Token):
    try:
        payload = jwt.decode(token.token_val, TokenController.jwt_secret_key, algorithms=[TokenController.algorithm])
        if 'sub' not in payload:
            raise HTTPException(status_code=401)
        result = await Tokens.delete_one({'token_val':token})
        if result.deleted_count == 0:
            raise HTTPException(status_code=404)
    except JWTError:
        raise HTTPException(status_code=401)
