from datetime import datetime
from typing import Optional

from fastapi import APIRouter
from sqlmodel import Field, SQLModel

from ...db import get_session

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()

class HistoryGalleryOr(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    history_id: int
    visibility_level_id: int
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


class HistoryGalleryOrImage(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    history_gallery_or_id = int
    path: str
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


class HistoryGalleryOrImageTag(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    history_gallery_or_image_id: int
    gallery_opd_tag_id: int
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


class GalleryOrTag(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    status: bool
    name: str
