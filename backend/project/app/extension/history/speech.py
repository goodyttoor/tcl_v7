sfrom typing import Optional

from sqlmodel import Field, SQLModel


class HistorySpeech(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    history_id: int
    speech_clinic: bool
    speech_memo: str
    