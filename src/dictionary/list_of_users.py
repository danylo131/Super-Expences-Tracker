from models import user, User
from functions import GeneratorId

__all__ = ["print_availables_users", "add_new_user", "delete_user", "set_users_from_rep"]

users: dict[str, user.User] = {}
list_of_id = {""}

    

# def set_users_from_rep():
#     users = 

def print_availables_users():
    for id in users.keys():
        print(id, end="")

def add_new_user():
    new_id = GeneratorId.get(list_of_id)

    list_of_id.add(new_id)
    users[new_id] = User(new_id)

def delete_user(id: str):
    ...