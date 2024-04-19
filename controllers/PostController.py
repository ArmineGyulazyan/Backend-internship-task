from Models import Post
from Services import Posts


async def create_post(post:Post):
    await Posts.find_one({'user_id':post.post_id})


async def get_posts():
    return Posts.find()


def get_post(post_id:int):
    post = Posts.find({'user_id':post_id})
    if post:
        return post
    raise Exception('Such user does not exist')


async def update_post(post_id:int, new_params:dict):
    updated_post = await Posts.find_one_and_update({'post_id': post_id},{"$set":new_params})
    if not updated_post:
        raise Exception('Such user does not exist')


async def delete_post(post_id:int):
    deleted_post = await Posts.find_one_and_delete({'post_id': post_id})
    if not deleted_post:
        raise Exception('Such user does not exist')
