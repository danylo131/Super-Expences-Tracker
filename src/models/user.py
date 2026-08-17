from decimal import Decimal, InvalidOperation, ROUND_HALF_EVEN

class User:

    def __init__(self, user_id: str, balance: str | int | Decimal = '0.00'):
        self.id = user_id
        self.balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance):
        if isinstance(balance, float):
            raise TypeError()

        try:
            converted_balance = Decimal(balance)
        except InvalidOperation:
            raise ValueError()

        #if converted_balance < 0: raise ValueError() === ??????

        self._balance = converted_balance.quantize(Decimal('0.01'), ROUND_HALF_EVEN)