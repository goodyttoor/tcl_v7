from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


class Disease(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str


class DiseaseGroup(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str


class DiseaseGroupMap(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    disease_group_id: int
    disease_id: int


class PatientDisease(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    patient_id: int
    doctor_id: Optional[int] = None
    cleft: bool
    craniofacial: bool
    syndronic: bool
    non: bool
    comorbidity: bool
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


class PatientDiseaseList(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    patient_disease_id: int
    disease_id: int
    detail: str
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


class PatientDiseaseCleft(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    patient_disease_id: int
    cleft_type: str
    cleft_lateral: str
    cleft_side: str
    cleft_complete: str
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


class PatientDiseaseCraniofacial(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    patient_disease_id: int
    micrognathia_detail: str
    craniofacial_cleft_right: int
    craniofacial_cleft_medial: int
    craniofacial_cleft_left: int
    feem_nasofrontal: bool
    feem_nasofrontal_side: str
    feem_nasoethmoidal: bool
    feem_nasoethmoidal_side: str
    feem_mix: bool
    feem_mix_side: str
    feem_mix_detail: str
    craniofacial_microsomia_side: str
    craniofacial_microsomia_detail: str
    microtia_side: str
    microtia_detail: str
    craniosynostosis_detail: str
    frontonasal_dysplasia_detail: str
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None


class PatientDiseaseOther(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    patient_disease_id: int
    disease_group_id: int
    name: str
    detail: str
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: Optional[int] = None
