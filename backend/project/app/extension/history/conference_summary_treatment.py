from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


class HistorySummaryTreatmentConference(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    history_id_order: int
    history_id_conference: int
    summary_treatment_conference_id: int
    state: str
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


class SummaryTreatmentConference(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    problem: str
    question: str
    summary_plan: str
    surgeon_summary: str
    pre_operation_abg: bool
    post_operation_abg: bool
    pre_operation_redo_abg: bool
    pre_operation_jaw_surgery: bool
    pre_operation_computing_design: bool
    pre_operation_3d_print: bool
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


class SummaryTreatmentConferenceDoctorMap(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    summary_treatment_conference_id: int
    doctor_id: int
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None
