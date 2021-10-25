import copy
from datetime import datetime, date
from decimal import Decimal
from typing import Optional, List

from fastapi import APIRouter, Depends, HTTPException, status, File, UploadFile
from fastapi.encoders import jsonable_encoder
from sqlmodel import Field, SQLModel

from ..db import get_session

from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    state: str  # Statue: pending, active, inactive
    id_type_id: int
    id_number: str = None
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


@router.post("/user", response_model=User)
async def create_user(user: User, session: AsyncSession = Depends(get_session)):
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user


@router.get("/user", response_model=List[User])
async def get_users(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(User))
    users = result.scalars().all()
    return users


@router.post("/user/check_id/{id_type_id}/{id_number}", response_model=bool)
async def check_id_available(id_type_id: int, id_number: str, session: AsyncSession = Depends(get_session)):
    # Check id existence
    users = await session.execute(select(User).where(User.id_type_id == id_type_id).where(User.id_number == id_number))
    if users is None:
        return True
    return False


@router.get("/user/pending_num", response_model=int)
async def get_pending_user_num(session: AsyncSession = Depends(get_session)):
    # Get user with pending status
    users = await session.execute(select(User).where(User.state == "pending"))
    return len(users.scalars().all())


@router.get("/user/{user_id}", response_model=User)
async def get_user(user_id: int, session: AsyncSession = Depends(get_session)):
    # Get user with id
    users = await session.execute(select(User).where(User.id == user_id))
    user = users.scalars().first()
    return user


@router.put("/user/{user_id}", response_model=User)
async def update_user(user_id: int, user: User, session: AsyncSession = Depends(get_session)):
    # Get user with id
    statement = select(User).where(User.id == user_id)
    users = await session.execute(statement)

    # Update detail
    user_old = users.one()
    model = User(**user_old)
    update_data = user.dict(exclude_unset=True)
    updated_user = model.copy(update=update_data)
    user_old = jsonable_encoder(updated_user)

    # Commit to database
    await session.commit()

    return user_old


@router.delete("/user/{user_id}")
async def delete_user(user_id: int, session: AsyncSession = Depends(get_session)):
    # Check user existence
    statement = select(User).where(User.id == user_id)
    user = await session.execute(statement)

    # Not found error
    if not user:
        raise HTTPException(status_code=404, detail='User not found')

    user = user.scalars().one()

    # Delete
    await session.delete(user)
    await session.commit()

    return status.HTTP_200_OK


@router.post("/user/{user_id}/cert")
async def upload_cert(file: UploadFile = File(...), session: AsyncSession = Depends(get_session)):
    return {"filename": file.filename}


@router.post("/user/{user_id}/accept")
async def accept_policy(session: AsyncSession = Depends(get_session)):
    return None


@router.post("/user/{user_id}/reset")
async def reset_password(session: AsyncSession = Depends(get_session)):
    return None


@router.post("/user/{user_id}/avatar")
async def upload_avatar(session: AsyncSession = Depends(get_session)):
    return None


@router.delete("/user/{user_id}/avatar")
async def delete_avatar(session: AsyncSession = Depends(get_session)):
    return None


@router.post("/user/{user_id}/role")
async def set_role(session: AsyncSession = Depends(get_session)):
    return None


@router.post("/user/feedback")
async def create_user_feedback(session: AsyncSession = Depends(get_session)):
    return None


@router.get("/user/feedback")
async def get_user_feedbacks(session: AsyncSession = Depends(get_session)):
    return None


@router.get("/user/feedback/{feedback_id}")
async def get_user_feedback(session: AsyncSession = Depends(get_session)):
    return None


@router.put("/user/feedback/{feedback_id}")
async def update_user_feedback(session: AsyncSession = Depends(get_session)):
    return None


@router.post("/user/doctor")
async def create_doctor(session: AsyncSession = Depends(get_session)):
    return None


@router.get("/user/doctor")
async def get_doctors(session: AsyncSession = Depends(get_session)):
    return None


@router.get("/user/doctor/{doctor_id}")
async def get_doctor(session: AsyncSession = Depends(get_session)):
    return None


@router.put("/user/doctor/{doctor_id}")
async def update_doctor(session: AsyncSession = Depends(get_session)):
    return None


@router.delete("/user/doctor/{doctor_id}")
async def delete_doctor(session: AsyncSession = Depends(get_session)):
    return None
