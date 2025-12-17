from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class USSDRequest(BaseModel):
    session_id: str
    phone_number: str
    text: str

class USSDResponse(BaseModel):
    response: str

@router.post("/ussd", response_model=USSDResponse)
async def handle_ussd_request(ussd_request: USSDRequest):
    # Logic to handle USSD request goes here
    # This is a placeholder response
    response_text = "Welcome to the Hepatitis B adherence system. Please select an option."
    
    return USSDResponse(response=response_text)