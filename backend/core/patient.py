from datetime import datetime, date, time
from decimal import Decimal
from typing import Optional

from fastapi import APIRouter
from sqlmodel import Field, SQLModel

router = APIRouter()


class Patient(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email = str
    email_verified_at: Optional[datetime] = None
    password: str
    remember_token: str
    first_name_thai: str
    last_name_thai: str
    first_name_english: str
    last_name_english: str
    race_id: Optional[int] = None
    religion_id: Optional[int] = None
    occupation_id: Optional[int] = None
    marital_status_id: Optional[int] = None
    birth_date: date
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
    blood_group: str
    allergy: str
    right_primary: str
    right_secondary: str
    right_national_hospital_id: Optional[int] = None
    right_dmis_code: str
    right_other: str
    consent_path: str
    consent_signature: str
    patient_source_id: str
    policy_accept: bool
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


class PatientPhone(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    patient_id: int
    number: str
    detail: str
    receive_sms: bool
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


class PatientLanguage(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    patient_id: int
    language_id: int
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


class PatientIdNumber(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    patient_id: int
    id_type_id: int
    number: str
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


class PatientDoctorMap(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    patient_id: int
    doctor_id: int
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


class PatientHospitalMap(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    patient_id: int
    hospital_id: int
    primary: bool
    hospital_number: str
    travel_distance: float
    travel_time: time
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


class PatientNotification(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    patient_id: int
    name: str
    detail: str
    is_read: bool
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


class PatientSource(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    created_at: datetime
    created_by: int


class PatientTag(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    created_at: datetime
    created_by: int
