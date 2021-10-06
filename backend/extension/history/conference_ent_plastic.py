from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


class HistoryEntPlasticConference(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    history_id_order: int
    history_id_conference: int
    ent_plastic_conference_id: int
    state: str
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


class EntPlasticConference(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    problem: str
    question: str
    ent_plan: str
    surgeon_plant: str
    post_plan: str
    surgeon_post_plan: str
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


class EntPlasticConferenceDoctorMap(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    ent_plastic_conference_id: int
    doctor_id: int
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None
