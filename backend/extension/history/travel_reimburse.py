from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


class HistoryTravelReimburse(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    history_id: int
    history_procedure_id: int
    group: str
    guardian_id: Optional[int] = None
    procedure_id: int
    amount: float
    detail: str
    pdf_path: str
    signature_path: str
    document_path: str
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None
