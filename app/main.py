from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import models
from .database import engine, Base
from .routers import user, auth, admin


models.Base.metadata.create_all(bind=engine)
# Alembic working insted of this enginee

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(admin.router)
#app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "Hello World"}

# # Create tables on startup
# @app.on_event("startup")
# def on_startup():
#     Base.metadata.create_all(bind=engine)



    