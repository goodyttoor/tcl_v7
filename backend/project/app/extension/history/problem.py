from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


class HistoryProblem(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    history_id: int
    detail: str
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None
