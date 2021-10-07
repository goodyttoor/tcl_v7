from datetime import datetime, date, time
from typing import Optional

from sqlmodel import Field, SQLModel


class HistoryAppointmentOpd(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    history_id: int
    appointment_opd_id: int
    state_from: str
    state_to: str
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


class HistoryAppointmentOpdMap(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    appointment_opd_id: int
    procedure_id: int
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


class AppointmentOpd(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    state: str
    date_visit: date
    date_confirmation: date
    time_start: time
    time_end: time
    detail: str
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


class AppointmentOpdReschedule(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    appointment_opd_id: int
    date_from: date
    date_to: date
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


class AppointmentOpdDoctorMap(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    appointment_opd_id: int
    doctor_id: int
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None
