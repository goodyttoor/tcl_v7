from datetime import datetime
from typing import Optional

from fastapi import APIRouter, Depends
from sqlmodel import Field, SQLModel

from ...db import get_session

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


router = APIRouter()


class HistorySummaryTreatmsummaryConference(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    history_id_order: int
    history_id_conference: int
    summary_treatmsummary_conference_id: int
    state: str
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


class SummaryTreatmsummaryConference(SQLModel, table=True):
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


class SummaryTreatmsummaryConferenceDoctorMap(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    summary_treatmsummary_conference_id: int
    doctor_id: int
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


@router.post("/history_summary_conference", response_model=HistorySummaryTreatmsummaryConference)
async def create_history_summary_conference(history_summary_conference: HistorySummaryTreatmsummaryConference, session: AsyncSession = Depends(get_session)):
    session.add(history_summary_conference)
    await session.commit()
    await session.refresh(history_summary_conference)
    return history_summary_conference


@router.post("/summary_conference", response_model=SummaryTreatmsummaryConference)
async def create_summary_conference(summary_conference: SummaryTreatmsummaryConference, session: AsyncSession = Depends(get_session)):
    session.add(summary_conference)
    await session.commit()
    await session.refresh(summary_conference)
    return summary_conference


@router.get("/history_summary_conference/{id}", response_model=HistorySummaryTreatmsummaryConference)
async def get_history_summary_conference(id: int, session: AsyncSession = Depends(get_session)):
    history_summary_conferences = await session.execute(select(HistorySummaryTreatmsummaryConference).where(HistorySummaryTreatmsummaryConference.id == id))
    history_summary_conference = history_summary_conferences.scalars().first()
    return history_summary_conference



@router.put("/history_summary_conference/{id}", response_model=HistorySummaryTreatmsummaryConference)
async def update_history_summary_conference(id: int, session: AsyncSession = Depends(get_session)):
    return None


@router.delete("/history_summary_conference/{id}")
async def delete_history_summary_conference(session: AsyncSession = Depends(get_session)):
    return None


@router.delete("/history_summary_conference/{id}")
async def delete_summary_conference(session: AsyncSession = Depends(get_session)):
    return None