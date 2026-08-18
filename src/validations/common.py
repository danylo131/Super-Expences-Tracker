import re

def validate_type(value, expected_type: type):
    if not isinstance(value, expected_type):
        raise TypeError()
    return value

def validate_patern(value: str, pattern: str) -> str:
    validate_type(value, str)
    if not re.match(pattern, value):
        raise ValueError()
    return value

def validate_exact_len(value: str, length: int) -> str:
    validate_type(value, str)
    if len(value) != length:
        raise ValueError()
    return value    