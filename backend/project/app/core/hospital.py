from datetime import datetime
from decimal import Decimal
from typing import Optional

from fastapi import APIRouter
from sqlmodel import Field, SQLModel


class Hospital(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    hospital_group_id: Optional[int] = None
    name: str
    code: str
    address_house_number: str
    address_moo: str
    address_soi: str
    address_road: str
    address_tambon_id: Optional[int] = None
    address_amphoe_id: Optional[int] = None
    address_province_id: Optional[int] = None
    address_other: str
    latitude: Decimal
    longitude: Decimal
    latitude_custom: Decimal
    longitude_custom: Decimal
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


class HospitalGroup(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    status: bool
    name: str
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


class HospitalProcedureMap(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    hospital_id: int
    procedure_id: int
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


class HospitalSameWeekProcedure(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    hospital_id_1: int
    hospital_id_2: int
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


class HospitalPhone(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    hospital_id: int
    number: str
    detail: str
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


class HospitalNode(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    hospital_id: int
    name: str
    day_of_week: int
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


class HospitalNodeDisciplineGroupMap(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    hospital_id: int
    discipline_group_id: int
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None
