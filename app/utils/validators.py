"""Request Validators"""
from datetime import datetime
from typing import Any
from pydantic import BaseModel


class UserRegistration(BaseModel):
    """User Registration Request Payload Validator"""
    email: str
    password: str
    created_at: datetime | None = None
    last_log_in: datetime | None = None


class CrudRequest(BaseModel):
    """Mongo Routes Request Payload Validator"""
    collection_name: str
    fields: dict | list[dict] | None = None
    field: str | None = None
    operator: str | None = None
    value: Any = None


class ExcuteQueryRequest(BaseModel):
    """Pre Defined Query Payload Validator"""
    collection_name: str
    pre_defined_query: str
    field: str | None = None
    limit_count: int | None = None
    fields: list | None = None
