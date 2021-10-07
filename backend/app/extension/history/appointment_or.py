from datetime import datetime, date, time
from typing import Optional

from sqlmodel import Field, SQLModel


class HistoryAppointmentOr(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    history_id: int
    appointment_or_id: int
    state_from: str
    state_to: str
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


class HistoryAppointmentOrMap(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    appointment_or_id: int
    procedure_id: int
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


class AppointmentOr(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    state: str
    date_procedure: date
    date_admission: date
    date_confirmation: date
    time_start: time
    time_end: time
    disease: str
    detail: str
    is_special_tool_required: bool
    is_icu_reserved: bool
    is_date_recorded: bool
    tool_note: str
    icu_note: str
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


class AppointmentOrReschedule(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    appointment_or_id: int
    date_from: date
    date_to: date
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


class AppointmentDoctorMap(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    appointment_or_id: int
    doctor_id: int
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None
