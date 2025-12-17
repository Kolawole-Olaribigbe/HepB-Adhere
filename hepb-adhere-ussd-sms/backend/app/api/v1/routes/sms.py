from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from app.services.twilio_client import send_sms

router = APIRouter()

class SMSRequest(BaseModel):
    phone_number: str
    message: str

@router.post("/send", response_model=dict)
async def send_sms_message(sms_request: SMSRequest):
    try:
        response = await send_sms(sms_request.phone_number, sms_request.message)
        return {"status": "success", "response": response}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/status/{message_id}", response_model=dict)
async def get_sms_status(message_id: str):
    try:
        # Logic to retrieve SMS status would go here
        # This is a placeholder for demonstration purposes
        return {"status": "delivered", "message_id": message_id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))