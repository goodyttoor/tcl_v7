from datetime import datetime, date
from decimal import Decimal
from typing import Optional, List

from fastapi import APIRouter, Depends
from sqlmodel import Field, SQLModel

from ...db import get_session

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()


class HistoryTravelReimburse(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    history_id: int
    history_procedure_id: int
    group: str
    guardian_id: Optional[int] = None
    procedure_id: int
    amount: float
    detail: str
    pdf_path: str
    signature_path: str
    document_path: str
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


@router.post("/history_travel_reimburse", response_model=HistoryTravelReimburse)
async def create_history_travel_reimburse(history_travel_reimburse: HistoryTravelReimburse, session: AsyncSession = Depends(get_session)):
    session.add(history_travel_reimburse)
    await session.commit()
    await session.refresh(history_travel_reimburse)
    return history_travel_reimburse


@router.get("/history_travel_reimburse/{id}", response_model=HistoryTravelReimburse)
async def get_history_travel_reimburse(id: int, session: AsyncSession = Depends(get_session)):
    history_travel_reimburses = await session.execute(select(HistoryTravelReimburse).where(HistoryTravelReimburse.id == id))
    history_travel_reimburse = history_travel_reimburses.scalars().first()
    return history_travel_reimburse


@router.put("/history_travel_reimburse/{id}", response_model=HistoryTravelReimburse)
async def update_history_travel_reimburse(id: int, session: AsyncSession = Depends(get_session)):
    return None


@router.delete("/history_travel_reimburse/{id}")
async def delete_history_travel_reimburse(session: AsyncSession = Depends(get_session)):
    return None


@router.get("/history_travel_reimburse/patient/{patient_id}", response_model=HistoryTravelReimburse)
async def get_history_travel_reimburse_patient(patient_id: int, session: AsyncSession = Depends(get_session)):
    history_id = await session.execute(select(HistoryTravelReimburse.id).where(HistoryTravelReimburse.patient_id == patient_id))
    history_travel_reimburses = await session.execute(select(HistoryTravelReimburse).where(HistoryTravelReimburse.history_id == history_id))
    history_travel_reimburse = history_travel_reimburses.scalars().first()
    return history_travel_reimburse


@router.get("/history_travel_reimburse", response_model=HistoryTravelReimburse)
async def get_history_travel_reimburse_daily(session: AsyncSession = Depends(get_session)):
    return None


@router.get("/history_travel_reimburse/{id}", response_model=HistoryTravelReimburse)
async def get_history_travel_reimburse_pdf(id: int, session: AsyncSession = Depends(get_session)):
    history_travel_reimburses = await session.execute(select(HistoryTravelReimburse.pdf_path).where(HistoryTravelReimburse.id == id))
    history_travel_reimburse = history_travel_reimburses.scalars().first()
    return history_travel_reimburse


@router.post("/history_travel_reimburse/{id}/document", response_model=HistoryTravelReimburse)
async def upload_document(session: AsyncSession = Depends(get_session)):
    return None


@router.post("/history_travel_reimburse/{id}/signature")
async def upload_signature(session: AsyncSession = Depends(get_session)):
    return None