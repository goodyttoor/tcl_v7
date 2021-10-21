from datetime import datetime
from typing import Optional

from fastapi import APIRouter, Depends
from sqlmodel import Field, SQLModel

from ...db import get_session

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


router = APIRouter()


class HistoryOrthoPlasticConference(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    history_id_order: int
    history_id_conference: int
    ortho_plastic_conference_id: int
    state: str
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


class OrthoPlasticConference(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    problem: str
    question: str
    ortho_plan: str
    maxillo_plan: str
    surgeon_plant: str
    post_plan: str
    surgeon_post_plan: str
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


class OrthoPlasticConferenceDoctorMap(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    ortho_plastic_conference_id: int
    doctor_id: int
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


@router.post("/history_ortho_conference", response_model=HistoryOrthoPlasticConference)
async def create_history_ortho_conference(history_ortho_conference: HistoryOrthoPlasticConference, session: AsyncSession = Depends(get_session)):
    session.add(history_ortho_conference)
    await session.commit()
    await session.refresh(history_ortho_conference)
    return history_ortho_conference


@router.post("/ortho_conference", response_model=OrthoPlasticConference)
async def create_ortho_conference(ortho_conference: OrthoPlasticConference, session: AsyncSession = Depends(get_session)):
    session.add(ortho_conference)
    await session.commit()
    await session.refresh(ortho_conference)
    return ortho_conference


@router.get("/history_ortho_conference/{id}", response_model=HistoryOrthoPlasticConference)
async def get_history_ortho_conference(id: int, session: AsyncSession = Depends(get_session)):
    history_ortho_conferences = await session.execute(select(HistoryOrthoPlasticConference).where(HistoryOrthoPlasticConference.id == id))
    history_ortho_conference = history_ortho_conferences.scalars().first()
    return history_ortho_conference



@router.put("/history_ortho_conference/{id}", response_model=HistoryOrthoPlasticConference)
async def update_history_ortho_conference(id: int, session: AsyncSession = Depends(get_session)):
    return None


@router.delete("/history_ortho_conference/{id}")
async def delete_history_ortho_conference(session: AsyncSession = Depends(get_session)):
    return None


@router.delete("/history_ortho_conference/{id}")
async def delete_ortho_conference(session: AsyncSession = Depends(get_session)):
    return None