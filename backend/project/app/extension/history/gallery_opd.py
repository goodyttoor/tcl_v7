from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


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
