from datetime import datetime, date
from typing import Optional

from sqlmodel import Field, SQLModel


class HistoryHomeVisit(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    history_id: int
    visit_date: date
    patient_id: int
    guardian_id: Optional[int] = None
    study_place: str
    study_level: str
    diagnosis: str
    diagnosis_other: str
    income: int
    travel_method: str
    travel_distance: str
    travel_problem: str
    travel_status: str
    cheilo_status: str
    cheilo_date_schedule: date
    cheilo_done_age: str
    cheilo_hospital_id: int
    palato_status: str
    palato_date_schedule: date
    palato_done_age: str
    palato_hospital_id: int
    speech_status: str
    speech_age_start: str
    speech_hospital: str
    speech_date_last: date
    audio_status: str
    audio_result: str
    audio_age: str
    audio_hospital_id: int
    dent_obtulator: bool
    dent_obtulator_hospital_id: int
    dent_obtulator_date: date
    dent_nasal_adjustor: bool
    dent_nasal_adjustor_hospital_id: int
    dent_nasal_adjustor_date: date
    dent_oral_care: bool
    dent_oral_care_hospital_id: int
    dent_oral_care_date: date
    dent_ortho: bool
    dent_ortho_hospital_id: int
    dent_ortho_date: date
    dent_other: bool
    dent_other_name: str
    dent_other_hospital_id: int
    dent_other_date: date
    paste: str
    paste_other: str
    brush_freq: str
    brush_method_rub: bool
    brush_method_updown: bool
    brush_method_bass: bool
    brush_method_other: str
    brush_other_flush_water: bool
    brush_other_flush_wash: bool
    brush_other_floss: bool
    brush_other_interdental: bool
    brush_other_none: bool
    brush_other: str
    freq_dent_visit: str
    stress_sleep_score: int
    stress_concentrate_score: int
    stress_irritate_score: int
    stress_bore_score: int
    stress_social_score: int
    feedback_post_treat: str
    feedback_problem: str
    feedback_need: str
    feedback_suggest: str
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


class HistoryHomeVisitImage(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    history_home_visit_id: int
    path: str
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None
