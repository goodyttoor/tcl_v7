from datetime import datetime, date
from decimal import Decimal
from typing import Optional, List

from fastapi import APIRouter, Depends
from sqlmodel import Field, SQLModel

from ...db import get_session

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()


class HistoryProblem(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    history_id: int
    detail: str
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


@router.post("/history_problem", response_model=HistoryProblem)
async def create_history_problem(history_problem: HistoryProblem, session: AsyncSession = Depends(get_session)):
    session.add(history_problem)
    await session.commit()
    await session.refresh(history_problem)
    return history_problem


@router.get("/history_problem/{id}", response_model=HistoryProblem)
async def get_history_problem(id: int, session: AsyncSession = Depends(get_session)):
    history_problems = await session.execute(select(HistoryProblem).where(HistoryProblem.id == id))
    history_problem = history_problems.scalars().first()
    return history_problem


@router.put("/history_problem/{id}", response_model=HistoryProblem)
async def update_history_problem(id: int, session: AsyncSession = Depends(get_session)):
    return None


@router.delete("/history_problem/{id}")
async def delete_history_problem(session: AsyncSession = Depends(get_session)):
    return None