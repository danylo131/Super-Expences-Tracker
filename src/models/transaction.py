import re
from decimal import Decimal, InvalidOperation, ROUND_HALF_EVEN

class Transaction:
    def __init__(self,  user_id : str, transaction_id : str, date, time,  type : str, comment : str, flag : str, amount : str | int | Decimal = '0.00',):
        self.user_id = user_id
        self.transaction_id = transaction_id
        self.date = date
        self.time = time
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
        if not isinstance(user_id, str):
            raise TypeError("Invalid UserID type(UserID must be a string)!")
        if not re.match(r"^[a-zA-Z]{4}\d{4}$", user_id):
            raise ValueError("Invalid UserID patern!")
        self._user_id = user_id

    @property
    def transaction_id(self) -> str:
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        if not isinstance(transaction_id, str):
            raise TypeError("Invalid TransactionID type(TransactionID must be a string)!")
        if not re.match(r"^[a-zA-Z]{4}\d{4}$", transaction_id):
            raise ValueError("Invalid TransactionID patern!")
        self._transaction_id = transaction_id

    ### ======= ЗАМІНИТИ ФЛОАТ на Decimal ВСЮДИ ДЕ БАЛАНС =======
    @property
    def amount(self) -> Decimal:
        return self._amount

    @amount.setter
    def amount(self, amount):
        if isinstance(amount, float):
            raise TypeError()
        try:
            converted_amount = Decimal(amount)
        except InvalidOperation:
            raise ValueError()

        if converted_amount < 0:
            raise ValueError()

        self._amount = converted_amount.quantize(Decimal('0.01'), rounding=ROUND_HALF_EVEN)   

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        if not isinstance(type, str):
            raise TypeError()
        if type.lenght != 1:
            raise ValueError()
        
        self._type = type

    @property
    def comment(self):
        return self._comment

    @comment.setter
    def comment(self, comment):
        if not isinstance(comment, str):
            raise TypeError()
        if comment.lenght != 1:
            raise ValueError()
        
        self._comment = comment

    @property
    def flag(self):
        return self._flag

    @flag.setter
    def flag(self, flag):
        if not isinstance(flag, str):
            raise TypeError()
        if flag.lenght != 1:
            raise ValueError()
        
        self._flag = flag
        
