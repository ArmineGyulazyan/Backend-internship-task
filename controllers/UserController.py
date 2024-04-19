from Models import User
from Services import Users
import bcrypt

def hash_psw(password:str):
    hashed_psw = bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt())
    return hashed_psw.decode('utf-8')


async def create_user(user:User):
    user_check = await Users.find_one({'user_id':user.user_id})
    if user_check:
        raise Exception('Trying to create an existing user')
    user.password = hash_psw(user.password)
    await Users.insert_one(user.dict())


async def get_users():
    return Users.find()


def get_user(user_mail:str):
    user = Users.find_one({'user_mail':user_mail})
    if user:
        return user
    raise Exception('Such user does not exist')


async def update_user(user_id:int, new_params:dict):
    if 'password' in new_params:
        new_params['password'] = hash_psw(new_params['password'])
    updated_user = await Users.find_one_and_update({'user_id': user_id},{"$set":new_params})
    if not updated_user:
        raise Exception('Such user does not exist')


async def delete_user(user_id:int):
    deleted_user = await Users.find_one_and_delete({'user_id': user_id})
    if not deleted_user:
        raise Exception('Such user does not exist')
