from decimal import Decimal
from validations.finance import validate_finance
from validations.common import validate_type, validate_exact_len
from validations.ids import validate_id_patern
from validations.time_date import validate_setter_time_date
from datetime import datetime

class Transaction:
    def __init__(self,  user_id : str, transaction_id : str, transaction_time_date: datetime,  type : str, comment : str, flag : str, amount : str | int | Decimal = '0.00',):
        self.user_id = user_id
        self.transaction_id = transaction_id
        self.transaction_time_date = transaction_time_date
        self.amount = amount
        self.type = type
        self.comment = comment
        self.flag = flag

    #Getters/setters
    @property
    def user_id(self) -> str:
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        self._user_id = validate_id_patern(user_id)

    @property
    def transaction_id(self) -> str:
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        self._transaction_id = validate_id_patern(transaction_id)

    @property
    def amount(self) -> Decimal:
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = validate_finance(amount)   

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, type):
        self._type = validate_exact_len(type, 1)

    @property
    def comment(self) -> str:
        return self._comment

    @comment.setter
    def comment(self, comment):
        self._comment = validate_type(comment, str)

    @property
    def flag(self) -> str: 
        return self._flag

    @flag.setter
    def flag(self, flag):
        self._flag = validate_exact_len(flag, 1)

    @property
    def transaction_time_date(self) -> datetime:
        return self._transaction_time_date

    @transaction_time_date.setter
    def transaction_time_date(self, value):
        self._transaction_time_date = validate_setter_time_date(value)