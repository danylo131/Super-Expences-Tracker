from datetime import datetime, timezone

def validate_setter_time_date(value):
    if isinstance(value, str):
        try:
            parsed_time_date = datetime.fromisoformat(value)
        except ValueError:
            raise ValueError()
    elif isinstance(value, datetime):
        parsed_time_date = value
    else:
        raise TypeError()

    if parsed_time_date.tzinfo is None:
        raise ValueError()

    current_time_date = datetime.now(timezone.utc)

    if parsed_time_date > current_time_date:
        raise ValueError

    return parsed_time_date

    