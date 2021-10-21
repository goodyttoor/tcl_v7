from datetime import datetime, date
from typing import Optional

from fastapi import APIRouter, Depends
from sqlmodel import Field, SQLModel

from ...db import get_session

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()


class HistoryVpi(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    history_id: int
    detail: str
    vpi_method: str
    velum_structure: str
    tonsil_enlargement_right: str
    tonsil_enlargement_left: str
    adenoid_hypertrophy_percent: int
    tonsilectomy_right: bool
    tonsilectomy_left: bool
    ademoidectomy: bool
    tongue_tie: bool
    tongue_tie_frenectomy: bool
    veloadenoid_clodure: str
    gap_type: str
    gap_length: str
    vpi: str
    speech_therapy: bool
    furlow_palatoplasty: bool
    furlow_palatoplasty_date: date
    sphincteroplasty: bool
    sphicteroplasty_date: date
    obturator: bool
    obturator_date: date
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


@router.post("/history_vpi", response_model=HistoryVpi)
async def create_history_vpi(history_vpi: HistoryVpi, session: AsyncSession = Depends(get_session)):
    session.add(history_vpi)
    await session.commit()
    await session.refresh(history_vpi)
    return history_vpi


@router.get("/history_vpi/{id}", response_model=HistoryVpi)
async def get_history_vpi(id: int, session: AsyncSession = Depends(get_session)):
    history_vpis = await session.execute(select(HistoryVpi).where(HistoryVpi.id == id))
    history_vpi = history_vpis.scalars().first()
    return history_vpi


@router.put("/history_vpi/{id}", response_model=HistoryVpi)
async def update_history_vpi(id: int, session: AsyncSession = Depends(get_session)):
    return None


@router.delete("/history_vpi/{id}")
async def delete_history_vpi(session: AsyncSession = Depends(get_session)):
    return None