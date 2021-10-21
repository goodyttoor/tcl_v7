from decimal import Decimal
from typing import Optional, List

from fastapi import APIRouter, Depends
from sqlmodel import Field, SQLModel

from ...db import get_session

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()

class HistorySpeech(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    history_id: int
    speech_clinic: bool
    speech_memo: str


@router.post("/history_speech", response_model=HistorySpeech)
async def create_history_speech(history_speech: HistorySpeech, session: AsyncSession = Depends(get_session)):
    session.add(history_speech)
    await session.commit()
    await session.refresh(history_speech)
    return history_speech


@router.get("/history_speech/{id}", response_model=HistorySpeech)
async def get_history_speech(id: int, session: AsyncSession = Depends(get_session)):
    history_speeches = await session.execute(select(HistorySpeech).where(HistorySpeech.id == id))
    history_speech = history_speeches.scalars().first()
    return history_speech


@router.put("/history_speech/{id}", response_model=HistorySpeech)
async def update_history_speech(id: int, session: AsyncSession = Depends(get_session)):
    return None


@router.delete("/history_speech/{id}")
async def delete_history_speech(session: AsyncSession = Depends(get_session)):
    return None