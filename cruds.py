def db_get_all_hobby():
    return [{"id":10, "name": "Anime", "discription": "abcs", "avatar_link": "www.lo.com", "chat_id": "333"},
    {"id":11, "name": "Gym", "discription": "strong", "avatar_link": "www.ddddd.com", "chat_id": "55"}]

def db_add_user_discription(tg_login: str, discription: str):
    pass

def db_add_user_hobby(tg_login: str, hobby_id: int):
    pass

def db_get_user(user_tg_login):
    return {
        "name": "Dima",
        "hobby": [{"id":10, "name": "Anime", "discription": "abcs", "avatar_link": "www.lo.com", "chat_id": "0"}]
    }