from datetime import datetime, date
from decimal import Decimal
from typing import Optional, List

from fastapi import APIRouter, Depends
from sqlmodel import Field, SQLModel

from ...db import get_session

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()


class HistoryChiefComplaint(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    history_id: int
    detail: str
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


@router.post("/history_chief_complaint", response_model=HistoryChiefComplaint)
async def create_history_chief_complaint(history_chief_complaint: HistoryChiefComplaint, session: AsyncSession = Depends(get_session)):
    session.add(history_chief_complaint)
    await session.commit()
    await session.refresh(history_chief_complaint)
    return history_chief_complaint


@router.get("/history_chief_complaint/{id}", response_model=HistoryChiefComplaint)
async def get_history_chief_complaint(id: int, session: AsyncSession = Depends(get_session)):
    history_chief_complaints = await session.execute(select(HistoryChiefComplaint).where(HistoryChiefComplaint.id == id))
    history_chief_complaint = history_chief_complaints.scalars().first()
    return history_chief_complaint


@router.put("/history_chief_complaint/{id}", response_model=HistoryChiefComplaint)
async def update_history_chief_complaint(id: int, session: AsyncSession = Depends(get_session)):
    return None


@router.delete("/history_chief_complaint/{id}")
async def delete_history_chief_complaint(session: AsyncSession = Depends(get_session)):
    return None