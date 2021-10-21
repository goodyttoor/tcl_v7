from datetime import datetime, date
from decimal import Decimal
from typing import Optional, List

from fastapi import APIRouter, Depends
from sqlmodel import Field, SQLModel

from ...db import get_session

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()

class HistoryTreatment(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    history_id: int
    detail: str
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


@router.post("/history_treatment", response_model=HistoryTreatment)
async def create_history_treatment(history_treatment: HistoryTreatment, session: AsyncSession = Depends(get_session)):
    session.add(history_treatment)
    await session.commit()
    await session.refresh(history_treatment)
    return history_treatment


@router.get("/history_treatment/{id}", response_model=HistoryTreatment)
async def get_history_treatment(id: int, session: AsyncSession = Depends(get_session)):
    history_treatments = await session.execute(select(HistoryTreatment).where(HistoryTreatment.id == id))
    history_treatment = history_treatments.scalars().first()
    return history_treatment


@router.put("/history_treatment/{id}", response_model=HistoryTreatment)
async def update_history_treatment(id: int, session: AsyncSession = Depends(get_session)):
    return None


@router.delete("/history_treatment/{id}")
async def delete_history_treatment(session: AsyncSession = Depends(get_session)):
    return None
