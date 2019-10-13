from datetime import datetime


def validate_date(date_text, format="%Y-%m-%d"):
    try:
        datetime.strptime(date_text, format)
    except ValueError:
        raise ValueError(f"Incorrect data format, should be {format}")
