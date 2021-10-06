from datetime import date, datetime
from typing import Optional

from sqlmodel import Field, SQLModel


class HistoryRefer(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    history_id: int
    refer_id: int
    state: str
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


class Refer(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    source_user_id: int
    source_accept: bool
    source_detail: str
    target_user_id: int
    target_accept: bool
    target_detail: str
    refer_type_id: int
    reschedule_times: int
    state: str
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


class ReferProcedureMap(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    refer_id: int
    procedure_id: int
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


class ReferReschedule(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    refer_id: int
    from_date: date
    to_date: date
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None
