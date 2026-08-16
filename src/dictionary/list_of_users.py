from models import user
import string
import random

__all__ = ["print_availables_users", "add_new_user", "delete_user", "set_users_from_rep"]

users: dict[str, user.User] = {}
list_of_id = {""}

def generate_uniq_id() -> str:
    new_id = ""
    letters = string.ascii_letters
    numbers = string.digits

    while new_id in list_of_id:
        new_id = random.choice(letters, len=4) + random.choice(numbers, len=4)

    return new_id
    

# def set_users_from_rep():
#     users = 

def print_availables_users():
    for id in users.keys():
        print(id, end="")

def add_new_user():
    new_id = generate_uniq_id()

    list_of_id.add(new_id)
    users[new_id] = User(new_id)

def delete_user(id: str):
