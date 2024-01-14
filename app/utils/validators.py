from datetime import datetime
from pydantic import BaseModel


class UserRegistration(BaseModel):
    email: str
    password: str
    created_at: datetime | None = None
    last_log_in: datetime | None = None

class RecordRequest(BaseModel):
    collection_name: str
    record_id: str | None  = None