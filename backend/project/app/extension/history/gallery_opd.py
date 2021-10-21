from datetime import datetime

from typing import Optional

from fastapi import APIRouter, Depends
from sqlmodel import Field, SQLModel

from ...db import get_session

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()


class HistoryGalleryOpd(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    history_id: int
    visibility_level_id: int
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


class HistoryGalleryOpdImage(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    history_gallery_opd_id = int
    path: str
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


class HistoryGalleryOpdImageTag(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    history_gallery_opd_image_id: int
    gallery_opd_tag_id: int
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


class GalleryOpdTag(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    status: bool
    name: str



@router.post("/gallery_opd", response_model=HistoryGalleryOpd)
async def create_gallery_opd(history_gallery_opd: HistoryGalleryOpd, session: AsyncSession = Depends(get_session)):
    session.add(history_gallery_opd)
    await session.commit()
    await session.refresh(history_gallery_opd)
    return history_gallery_opd


@router.post("/gallery_item_opd", response_model=HistoryGalleryOpdImage)
async def create_gallery_item_opd(history_gallery_item_opd: HistoryGalleryOpdImage, session: AsyncSession = Depends(get_session)):
    session.add(history_gallery_item_opd)
    await session.commit()
    await session.refresh(history_gallery_item_opd)
    return history_gallery_item_opd


@router.delete("/gallery_opd/{id}")
async def delete_gallery_opd(session: AsyncSession = Depends(get_session)):
    return None


@router.delete("/gallery_item_opd/{id}")
async def delete_gallery_item_opd(session: AsyncSession = Depends(get_session)):
    return None


@router.put("/gallery_opd/{id}", response_model=HistoryGalleryOpd)
async def update_gallery_opd(id: int, session: AsyncSession = Depends(get_session)):
    return None


@router.put("/gallery_item_opd/{id}", response_model=HistoryGalleryOpdImage)
async def update_gallery_item_opd(id: int, session: AsyncSession = Depends(get_session)):
    return None


@router.get("/gallery_item_opd/{id}", response_model=HistoryGalleryOpdImage)
async def get_gallery_item_opd(id: int, session: AsyncSession = Depends(get_session)):
    items_opd = await session.execute(select(HistoryGalleryOpdImage).where(HistoryGalleryOpdImage.id == id))
    item_opd = items_opd.scalars().first()
    return item_opd


@router.post("/gallery_item_opd/{id}")
async def upload_opd_image(session: AsyncSession = Depends(get_session)):
    return None