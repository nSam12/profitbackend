from database import User, Groups, Hobby, RandomCoffee, engine
from sqlalchemy import select, insert
from sqlalchemy.orm import Session



session = Session(bind=engine)


def db_get_all_hobby():
    # return [{"id":10, "name": "Anime", "discription": "abcs", "avatar_link": "www.lo.com", "chat_id": "333"},
    # {"id":11, "name": "Gym", "discription": "strong", "avatar_link": "www.ddddd.com", "chat_id": "55"}]
    return [{'name' : select(Hobby.name), 'id' : select(Hobby.id), 'chat_id' : select(Hobby.chat_id), 'avatar_link' : select(Hobby.avatar_link)}]

def db_add_user_discription(tg_login: str, discription: str):
    user = User(tg_login=tg_login, discription=discription)
    with Session(autoflush=False, bind=engine) as session:
        session._update_impl(user)
        session.commit()
    return insert(User).values([{'tg_login' : tg_login, 'discription' : discription}])

def db_add_user_hobby(tg_login: str, hobby_id: int):
    return insert(User).values([{'tg_login': tg_login, 'id' : hobby_id}])

def db_get_user(user_tg_login):
    return {
        "name": select(User.tg_login),
        "hobby": [{"id":select(Hobby.id), "name": select(Hobby.name), "discription": select(Hobby.discription), "avatar_link": select(Hobby.avatar_link), "chat_id": select(Hobby.chat_id)}]
    }