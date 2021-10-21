from datetime import datetime
from typing import Optional

from fastapi import APIRouter, Depends
from sqlmodel import Field, SQLModel

from ..db import get_session

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

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
    procedure_id: int
    disease_id: bool
    require: bool
    age_min: float
    age_max: float


class HistoryProcedure(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    history_id: int
    procedure_id: int
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

#
#
# @router.post("/history_procedure", response_model=HistoryProcedure)
# async def create_history_procedure(history_procedure: HistoryProcedure, session: AsyncSession = Depends(get_session)):
#     session.add(history_procedure)
#     await session.commit()
#     await session.refresh(history_procedure)
#     return history_procedure
#
#
# @router.get("/history_procedure/{procedure_id}", response_model=HistoryProcedure)
# async def get_history_procedure(procedure_id: int, session: AsyncSession = Depends(get_session)):
#     history_procedures = await session.execute(select(HistoryProcedure).where(HistoryProcedure.id == procedure_id))
#     history_procedure = history_procedures.scalars().first()
#     return history_procedure
#
#
# @router.put("/history_procedure/{procedure_id}", response_model=HistoryProcedure)
# async def update_history_procedure(id: int, session: AsyncSession = Depends(get_session)):
#     return None
#
#
# @router.delete("/history_procedure/{procedure_id}")
# async def delete_history_procedure(session: AsyncSession = Depends(get_session)):
#     return None