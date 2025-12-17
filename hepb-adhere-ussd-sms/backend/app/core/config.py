from typing import Optional
from pydantic import BaseSettings


class Settings(BaseSettings):
    # Database configuration
    DATABASE_URL: str
    # Twilio configuration
    TWILIO_ACCOUNT_SID: str
    TWILIO_AUTH_TOKEN: str
    TWILIO_PHONE_NUMBER: str
    # Redis configuration
    REDIS_URL: str
    # Other configurations
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Observability / logging
    LOG_LEVEL: str = "INFO"
    LOG_JSON: bool = False
    SENTRY_DSN: Optional[str] = None
    METRICS_ENABLED: bool = True

    class Config:
        env_file = ".env"


settings = Settings()