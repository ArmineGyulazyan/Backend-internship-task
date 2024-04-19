from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
import bcrypt
from controllers.UserController import get_user, hash_psw


jwt_secret_key = '15ca8243fae36f9179396184cbc1b7d462db36232e453c3944c448804e3f6862'
# print(jwt_secret_key)
access_jwt_active_minutes = 1440
algorithm = 'HS256'

oauth_scheme = OAuth2PasswordBearer(tokenUrl='token')


def create_access_token(data:dict, active_time:timedelta|None=None):
    encoded = data.copy()
    if active_time is None:
        active_time = timedelta(minutes=access_jwt_active_minutes)

    expire = datetime.now(timezone.utc) + active_time
    encoded.update({'exp':expire})
    encoded_jwt = jwt.encode(encoded, jwt_secret_key, algorithm=algorithm)
    return encoded_jwt


async def authenticate_user(user_mail:str, password:str):
    user = await get_user(user_mail)
    # print(user.to_list(length=None))
    if bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
        return user


async def get_current_user(token:str=Depends(oauth_scheme)):
    try:
        payload = jwt.decode(token, jwt_secret_key, algorithms=[algorithm])
        user_mail = payload.get('sub')
        if not user_mail:
            raise HTTPException(status_code=401)
        user = await get_user(user_mail)
        return user
    except JWTError:
        raise HTTPException(status_code=401)





