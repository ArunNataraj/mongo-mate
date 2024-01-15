from datetime import datetime
from pydantic import BaseModel
from typing import Any


class UserRegistration(BaseModel):
    email: str
    password: str
    created_at: datetime | None = None
    last_log_in: datetime | None = None


class RecordRequest(BaseModel):
    collection_name: str
    record_id: str | None = None


class ViewRecordRequest(BaseModel):
    collection_name: str
    field: str | None = None
    operator: str | None = None
    value: Any = None


class InsertRecordRequest(BaseModel):
    collection_name: str
    fields: dict | list[dict]
