from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from backend.app.db.base import Base

class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    phone_number = Column(String, unique=True, index=True)
    date_of_birth = Column(Date)
    adherence_status = Column(String)

    # Relationships can be defined here if needed
    # e.g., medications = relationship("Medication", back_populates="patient")