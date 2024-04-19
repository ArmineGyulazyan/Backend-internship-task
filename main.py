from fastapi import FastAPI
import uvicorn
from routes import UserRoutes, PostRoutes, Authentication


app = FastAPI()
app.include_router(UserRoutes.route)
app.include_router(PostRoutes.route)
app.include_router(Authentication.route)


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
