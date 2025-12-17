from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.services.twilio_client import TwilioClient
from app.services.ussd_session import USSDSession

def get_twilio_client() -> TwilioClient:
    return TwilioClient()

def get_ussd_session() -> USSDSession:
    return USSDSession()

def get_db_session() -> Session:
    db = get_db()
    try:
        yield db
    finally:
        db.close()