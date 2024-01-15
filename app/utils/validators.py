from datetime import datetime
from pydantic import BaseModel
from typing import Any


class UserRegistration(BaseModel):
    email: str
    password: str
    created_at: datetime | None = None
    last_log_in: datetime | None = None

class CrudRequest(BaseModel):
    collection_name: str
    fields: dict | list[dict] | None = None
    field: str | None = None
    operator: str | None = None
    value: Any = None