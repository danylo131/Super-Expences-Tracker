from decimal import Decimal
from validations.finance import validate_finance
from validations.common import validate_type
from validations.ids import validate_id_patern

class User:

    def __init__(self, name: str, login: str, email: str, hashed_pass : str, user_id: str, balance: str | int | Decimal = '0.00'):
        self.id = user_id
        self.balance = balance
        self.name = name
        self.login = login
        self.email = email
        self.hashed_pass = hashed_pass

    @property
    def balance(self) -> Decimal: 
        return self._balance

    @balance.setter
    def balance(self, balance):
        self._balance = validate_finance(balance)

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = validate_type(name, str)

    @property
    def login(self) -> str:
        return self._login

    @login.setter
    def login(self, login: str):
        self._login = validate_type(login, str)

    @property
    def email(self) -> str: 
        return self._email

    @email.setter
    def email(self, email: str):
        ...

    @property
    def user_id(self) -> str:
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        self._user_id = validate_id_patern(user_id)

    @property
    def hashed_pass(self) -> str:
        return self._hashed_pass

    @hashed_pass.setter
    def hashed_pass(self, hashed_pass : str):
        self._hashed_pass = validate_type(hashed_pass, str)
