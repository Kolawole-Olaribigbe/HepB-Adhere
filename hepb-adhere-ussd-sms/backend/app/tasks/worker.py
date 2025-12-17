from celery import Celery
from app.db.session import get_db
from app.services.twilio_client import send_sms
from app.services.ussd_session import manage_ussd_session

celery = Celery(__name__, broker='redis://localhost:6379/0')

@celery.task
def send_sms_task(phone_number, message):
    """Task to send an SMS message."""
    send_sms(phone_number, message)

@celery.task
def ussd_session_task(session_id, user_input):
    """Task to manage a USSD session."""
    manage_ussd_session(session_id, user_input)