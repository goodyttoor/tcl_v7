from datetime import datetime
from decimal import Decimal
from typing import Optional

from fastapi import APIRouter
from sqlmodel import Field, SQLModel

router = APIRouter()


class Guardian(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email = str
    email_verified_at: Optional[datetime] = None
    password: str
    remember_token: str
    first_name_thai: str
    last_name_thai: str
    first_name_english: str
    last_name_english: str
    occupation_id: Optional[int] = None
    gender: str
    is_thai_address: bool
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
    alive: bool
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


class GuardianPhone(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    guardian_id: int
    number: str
    detail: str
    receive_sms: bool
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


class GuardianIdNumber(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    guardian_id: int
    id_type_id: int
    number: str
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


class GuardianPatientMap(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    guardian_id: int
    patient_id: int
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


class GuardianNotification(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    guardian_id: int
    name: str
    detail: str
    is_read: bool
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None
