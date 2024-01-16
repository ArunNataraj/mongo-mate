"""Utils Methods"""
from datetime import datetime
from uuid import uuid4
from app.utils.constants import MONGO_ID


def get_current_utc_time():
    """This Method Provides UTC Time in String"""
    return datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")


def add_uuid_to_records(records: list):
    """This Method Adds UUID To The Records"""
    try:
        for record in records:
            if MONGO_ID not in record:
                record[MONGO_ID] = f"""{uuid4()}"""
        return records
    except Exception as ex:
        print(ex)
        return ex
