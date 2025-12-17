from pydantic import BaseModel
from typing import Optional

class PatientBase(BaseModel):
    name: str
    phone_number: str
    adherence_level: Optional[int] = None

class PatientCreate(PatientBase):
    pass

class PatientUpdate(PatientBase):
    pass

class Patient(PatientBase):
    id: int

    class Config:
        orm_mode = True