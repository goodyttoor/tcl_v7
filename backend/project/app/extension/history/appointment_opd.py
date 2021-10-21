from datetime import datetime, date , time
from typing import Optional, List

from fastapi import APIRouter, Depends
from sqlmodel import Field, SQLModel

from ...db import get_session

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()


class HistoryAppointmentOpd(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    history_id: int
    appointment_opd_id: int
    state_from: str
    state_to: str
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


class HistoryAppointmentOpdMap(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    appointment_opd_id: int
    procedure_id: int
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


class AppointmentOpd(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    state: str
    date_visit: date
    date_confirmation: date
    time_start: time
    time_end: time
    detail: str
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


class AppointmentOpdReschedule(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    appointment_opd_id: int
    date_from: date
    date_to: date
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


class AppointmentOpdDoctorMap(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    appointment_opd_id: int
    doctor_id: int
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


@router.post("/history_appointment_opd", response_model=HistoryAppointmentOpd)
async def create_history_appointment_opd(history_appointment_opd: HistoryAppointmentOpd, session: AsyncSession = Depends(get_session)):
    session.add(history_appointment_opd)
    await session.commit()
    await session.refresh(history_appointment_opd)
    return history_appointment_opd


@router.post("/appointment_opd", response_model=AppointmentOpd)
async def create_appointment_opd(appointment_opd: AppointmentOpd, session: AsyncSession = Depends(get_session)):
    session.add(appointment_opd)
    await session.commit()
    await session.refresh(appointment_opd)
    return appointment_opd


@router.get("/history_appointment_opd/{id}", response_model=HistoryAppointmentOpd)
async def get_history_appointment_opd(id: int, session: AsyncSession = Depends(get_session)):
    history_appointments_opd = await session.execute(select(HistoryAppointmentOpd).where(HistoryAppointmentOpd.id == id))
    history_appointment_opd = history_appointments_opd.scalars().first()
    return history_appointment_opd


@router.get("/history_appointment_opd/user/{user_id}", response_model=HistoryAppointmentOpd)
async def get_history_appointment_opd_user(user_id: int, session: AsyncSession = Depends(get_session)):
    history_appointments_opd = await session.execute(select(HistoryAppointmentOpd).where(HistoryAppointmentOpd.created_by == user_id))
    history_appointment_opd = history_appointments_opd.scalars().first()
    return history_appointment_opd


@router.put("/history_appointment_opd/{id}", response_model=HistoryAppointmentOpd)
async def update_history_appointment_opd(id: int, session: AsyncSession = Depends(get_session)):
    return None


@router.delete("/history_appointment_opd/{id}")
async def delete_history_appointment_opd(session: AsyncSession = Depends(get_session)):
    return None


@router.delete("/appointment_opd/{id}")
async def delete_appointment_opd(session: AsyncSession = Depends(get_session)):
    return None



