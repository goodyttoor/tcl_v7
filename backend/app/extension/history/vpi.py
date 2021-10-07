from datetime import datetime, date
from typing import Optional

from sqlmodel import Field, SQLModel


class HistoryVpi(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    history_id: int
    detail: str
    vpi_method: str
    velum_structure: str
    tonsil_enlargement_right: str
    tonsil_enlargement_left: str
    adenoid_hypertrophy_percent: int
    tonsilectomy_right: bool
    tonsilectomy_left: bool
    ademoidectomy: bool
    tongue_tie: bool
    tongue_tie_frenectomy: bool
    veloadenoid_clodure: str
    gap_type: str
    gap_length: str
    vpi: str
    speech_therapy: bool
    furlow_palatoplasty: bool
    furlow_palatoplasty_date: date
    sphincteroplasty: bool
    sphicteroplasty_date: date
    obturator: bool
    obturator_date: date
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None
