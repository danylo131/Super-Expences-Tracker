from decimal import Decimal, InvalidOperation, ROUND_HALF_EVEN

def validate_finance(amount) -> Decimal:
    if isinstance(amount, float):
        raise TypeError()
    try:
        converted_amount = Decimal(amount)
    except InvalidOperation:
        raise ValueError()
    if converted_amount < 0:
        raise ValueError()

    return converted_amount.quantize(Decimal('0.01'), rounding=ROUND_HALF_EVEN)
        