from fastapi import FastAPI, Path, Header, Body
from pydantic import BaseModel
from typing import Any, List
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from cruds import db_get_all_hobby, db_add_user_discription, db_get_user

app = FastAPI()


origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://194.87.147.11",
    "http://194.87.147.11:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserDiscription(BaseModel):
    tg_login: str
    discription: str

class UserHobby(BaseModel):
    tg_login: str
    hobby_id: str

class Hobby(BaseModel):
    id: int
    name: str
    discription: str
    avatar_link: str
    chat_id: str


class User(BaseModel):
    name: str
    hobby: List[Hobby]

#Получить список всех хобби
@app.get("/hobby", response_model=List[Hobby])
def get_all_hobby() -> Any:
    return db_get_all_hobby()

#К пользователю добавить описание
@app.post("/me/add_discription")
def add_discription(data: UserDiscription):
    db_add_user_discription(data.tg_login, data.discription)

#К пользователю добавить хобби
@app.post("/me/add_hobby")
def add_discription(data: UserHobby):
    db_add_user_discription(data.tg_login, data.hobby_id)

#Получить полностью пользователя
@app.get("/user/{user_tg_login}", response_model=User)
def get_user(user_tg_login):
    return db_get_user(user_tg_login)
