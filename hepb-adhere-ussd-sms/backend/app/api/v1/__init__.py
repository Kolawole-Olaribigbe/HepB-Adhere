# backend/app/api/v1/__init__.py

from fastapi import APIRouter

router = APIRouter()

from .routes import ussd, sms, patients

router.include_router(ussd.router, prefix="/ussd", tags=["ussd"])
router.include_router(sms.router, prefix="/sms", tags=["sms"])
router.include_router(patients.router, prefix="/patients", tags=["patients"])