from decimal import Decimal
from datetime import datetime, date
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
    language_elm: bool
    language_utah: bool
    language_other: bool
    language_result: str
    language_result_pass: str
    language_result_not_pass: str
    language_other: str
    hearing_right: str
    hearing_right_result: str
    hearing_right_sensorineural: bool
    hearing_right_conductive: bool
    hearing_right_mixed: bool
    hearing_right_detail: str
    hearing_left: str
    hearing_left_result: str
    hearing_left_sensorineural: bool
    hearing_left_conductive: bool
    hearing_left_mixed: bool
    hearing_left_detail: str
    breathing: str
    breathing_detail: str
    symmetry_lip: str
    symmetry_nose: str
    lip_movement: str
    oronasal_fistular: str
    oronasal_fistular_present_location: str
    oronasal_fistular_present_size_w: str
    oronasal_fistular_present_size_l: str
    velum_soft_palate_structure: str
    velum_soft_palate_function: str
    dental_carries: str
    dental_occlusion: str
    dental_occlusion_malocclusion: str
    tongue_position: str
    tongue_movement: str
    intelligibility_standard_articulation: str
    intelligibility_standard: str
    intelligibility_standard_normal: str
    intelligibility_standard_unintelligibility: str
    intelligibility_standard_unintelligibility_text: str
    intelligibility_conversation_speech: bool
    intelligibility_conversation: str
    intelligibility_conversation_normal: str
    intelligibility_conversation_unintelligibility: str
    intelligibility_conversation_unintelligibility_text: str
    resonance: str
    resonance_hyper: str
    resonance_nasal: str
    articulation: str
    articulation_text: str
    facial_grimace: str
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


@router.post("/history_speech", response_model=HistorySpeech)
async def create_history_speech(history_speech: HistorySpeech, session: AsyncSession = Depends(get_session)):
    session.add(history_speech)
    await session.commit()
    await session.refresh(history_speech)
    return history_speech


@router.get("/history_speech/{history_speech_id}", response_model=HistorySpeech)
async def get_history_speech(id: int, session: AsyncSession = Depends(get_session)):
    history_speeches = await session.execute(select(HistorySpeech).where(HistorySpeech.id == id))
    history_speech = history_speeches.scalars().first()
    return history_speech


@router.put("/history_speech/{history_speech_id}", response_model=HistorySpeech)
async def update_history_speech(history_speech_id: int, history_speech: HistorySpeech):
    return None


@router.delete("/history_speech/{history_speech_id}")
async def delete_history_speech(session: AsyncSession = Depends(get_session)):
    return None