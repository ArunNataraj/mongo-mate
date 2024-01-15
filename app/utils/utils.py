from datetime import datetime
from app.utils.constants import MONGO_ID
from uuid import uuid4


def get_current_utc_time():
    return datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")


def add_uuid_to_records(records: list):
    for record in records:
        if MONGO_ID not in record:
            record[MONGO_ID] = f"""{uuid4()}"""
    return records
