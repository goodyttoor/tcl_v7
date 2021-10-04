from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


class Right(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str


class Province(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str


class Amphoe(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    province_id: int
    name: str


class Tambon(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    amphoe_id: int
    name: str


class Religion(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str


class National(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str


class Occupation(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str


class MaritalStatus(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str


class AcademicDegree(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str


class Allergy(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str


class Vehicle(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str


class Language(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str


class Relationship(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str


class IdType(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str


class FeedbackType(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str


class VisibilityLevel(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str


class Module(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    detail: str
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


class ModuleFunction(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    detail: str
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None
