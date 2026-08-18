from .common import validate_patern
ID_PATERN = r"^[a-zA-Z]{4}\d{4}$"

def validate_id_patern(value: str) -> str:
    return validate_patern(value, ID_PATERN)