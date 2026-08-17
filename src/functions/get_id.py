import string
import random

class GeneratorId:
    @classmethod
    def get(list_of_ids) -> str:
        new_id = ""
        letters = string.ascii_letters
        numbers = string.digits

        while new_id in list_of_ids:
            new_id = random.choice(letters, len=4) + random.choice(numbers, len=4)

        return new_id