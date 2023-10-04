from sqlalchemy import select, text
from datetime import date


def get_shift_day(client_name, shift_day, endpoint_id):
    return text(f"SELECT * FROM sources\
                WHERE client_name='{client_name}' and shift_day='{shift_day}'\
                and endpoint_id={endpoint_id}")
