from datetime import datetime, date
from decimal import Decimal
from typing import Optional

from fastapi import APIRouter, Depends
from sqlmodel import Field, SQLModel, Session

from ..db import get_session

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    id_type_id: int
    id_number: Optional[str] = None
    email = str
    email_verified_at: Optional[datetime] = None
    password: str
    remember_token: str
    hospital_id: Optional[int] = None
    hospital_node_id: Optional[int] = None
    discipline_id: int
    first_name_thai: str
    last_name_thai: str
    first_name_english: str
    last_name_english: str
    nickname: str
    birth_date: date
    gender: str
    academic_degree: str
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
    potential: str
    avatar_path: str
    document_path: str
    policy_accept: bool
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


class UserPhone(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int
    number: str
    detail: str
    receive_sms: bool
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


class UserFeedback(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int
    feedback_type_id: Optional[int] = None
    detail: str
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


class UserNotification(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int
    name: str
    detail: str
    is_read: bool
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


class UserRole(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int
    role_id: int
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


class UserSource(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    created_at: datetime
    created_by: int


class UserLog(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int


class Doctor(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int
    hospital_id: int
    discipline_id: int
    prefix: str
    first_name: str
    last_name: str
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


class DoctorProcedureMap(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    doctor_id: int
    procedure_id: int
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


class Discipline(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    discipline_group_id: int
    name: str
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


class DisciplineGroup(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


class Role(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


class RoleModuleFunctionMap(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    role_id: int
    module_function_id: int
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


# @router.post("/user")
# async def create_user(user: User, session: Session = Depends(get_session())):
#     user = User()
#     session.add(user)
#     session.commit()
#     session.refresh(user)
#     return user
#
#
# @router.get("/user")
# async def get_users(session: Session = Depends(get_session())):
#     result = session.execute(select(User))
#     users = result.scalars().all()
#     return users
