from datetime import datetime, date , time
from typing import Optional, List

from fastapi import APIRouter, Depends
from sqlmodel import Field, SQLModel

from ...db import get_session

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()


class HistoryAppointmentOr(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    history_id: int
    appointment_or_id: int
    state_from: str
    state_to: str
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


class HistoryAppointmentOrMap(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    appointment_or_id: int
    procedure_id: int
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


class AppointmentOr(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    state: str
    date_procedure: date
    date_admission: date
    date_confirmation: date
    time_start: time
    time_end: time
    disease: str
    detail: str
    is_special_tool_required: bool
    is_icu_reserved: bool
    is_date_recorded: bool
    tool_note: str
    icu_note: str
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


class AppointmentOrReschedule(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    appointment_or_id: int
    date_from: date
    date_to: date
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


class AppointmentOrDoctorMap(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    appointment_or_id: int
    doctor_id: int
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


@router.post("/history_appointment_or", response_model=HistoryAppointmentOr)
async def create_appointment_or(history_appointment_or: HistoryAppointmentOr, session: AsyncSession = Depends(get_session)):
    session.add(history_appointment_or)
    await session.commit()
    await session.refresh(history_appointment_or)
    return history_appointment_or


@router.post("/appointment_or", response_model=AppointmentOr)
async def create_history_appointment_or(appointment_or: AppointmentOr, session: AsyncSession = Depends(get_session)):
    session.add(appointment_or)
    await session.commit()
    await session.refresh(appointment_or)
    return appointment_or


@router.get("/history_appointment_or/{id}", response_model=HistoryAppointmentOr)
async def get_history_appointment_or(id: int, session: AsyncSession = Depends(get_session)):
    history_appointments_or = await session.execute(select(HistoryAppointmentOr).where(HistoryAppointmentOr.id == id))
    history_appointment_or = history_appointments_or.scalars().first()
    return history_appointment_or


@router.get("/history_appointment_or/user/{user_id}", response_model=HistoryAppointmentOr)
async def get_history_appointment_or_user(user_id: int, session: AsyncSession = Depends(get_session)):
    history_appointments_or = await session.execute(select(HistoryAppointmentOr).where(HistoryAppointmentOr.created_by == user_id))
    history_appointment_or = history_appointments_or.scalars().first()
    return history_appointment_or


@router.put("/history_appointment_or/{id}", response_model=HistoryAppointmentOr)
async def update_history_appointment_or(id: int, session: AsyncSession = Depends(get_session)):
    return None


@router.delete("/history_appointment_or/{id}")
async def delete_history_appointment_or(session: AsyncSession = Depends(get_session)):
    return None


@router.delete("/appointment_or/{id}")
async def delete_appointment_or(session: AsyncSession = Depends(get_session)):
    return None


# @router.get("/history_appointment_or/history/{patient_id}", response_model=HistoryTravelReimburse)
# async def get_history_travel_reimburse_patient(patient_id: int, session: AsyncSession = Depends(get_session)):
#     history_id = await session.execute(select(HistoryTravelReimburse.id).where(HistoryTravelReimburse.patient_id == patient_id))
#     history_travel_reimburses = await session.execute(select(HistoryTravelReimburse).where(HistoryTravelReimburse.history_id == history_id))
#     history_travel_reimburse = history_travel_reimburses.scalars().first()
#     return history_travel_reimburse

