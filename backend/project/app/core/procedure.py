from datetime import datetime
from typing import Optional

from fastapi import APIRouter
from sqlmodel import Field, SQLModel

router = APIRouter()


class Procedure(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    procedure_group_id: int
    parent_procedure_id: int
    name: str
    detail: str
    icd_9: str
    icd_10: str


class ProcedureGroup(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str


class ProcedureDiseaseMap(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    procedure_id: id
    disease_id: bool
    require: bool
    age_min: float
    age_max: float


class HistoryProcedure(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    history_id: id
    procedure_id: id
    detail: str
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


class HistoryProcedureDoctorMap(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    history_procedure_id: int
    doctor_id: int
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None
