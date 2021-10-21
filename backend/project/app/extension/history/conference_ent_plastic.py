from datetime import datetime
from typing import Optional

from fastapi import APIRouter, Depends
from sqlmodel import Field, SQLModel

from ...db import get_session

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


router = APIRouter()


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


@router.post("/history_ent_conference", response_model=HistoryEntPlasticConference)
async def create_history_ent_conference(history_ent_conference: HistoryEntPlasticConference, session: AsyncSession = Depends(get_session)):
    session.add(history_ent_conference)
    await session.commit()
    await session.refresh(history_ent_conference)
    return history_ent_conference


@router.post("/ent_conference", response_model=EntPlasticConference)
async def create_ent_conference(ent_conference: EntPlasticConference, session: AsyncSession = Depends(get_session)):
    session.add(ent_conference)
    await session.commit()
    await session.refresh(ent_conference)
    return ent_conference


@router.get("/history_ent_conference/{id}", response_model=HistoryEntPlasticConference)
async def get_history_ent_conference(id: int, session: AsyncSession = Depends(get_session)):
    history_ent_conferences = await session.execute(select(HistoryEntPlasticConference).where(HistoryEntPlasticConference.id == id))
    history_ent_conference = history_ent_conferences.scalars().first()
    return history_ent_conference



@router.put("/history_ent_conference/{id}", response_model=HistoryEntPlasticConference)
async def update_history_ent_conference(id: int, session: AsyncSession = Depends(get_session)):
    return None


@router.delete("/history_ent_conference/{id}")
async def delete_history_ent_conference(session: AsyncSession = Depends(get_session)):
    return None


@router.delete("/history_ent_conference/{id}")
async def delete_ent_conference(session: AsyncSession = Depends(get_session)):
    return None