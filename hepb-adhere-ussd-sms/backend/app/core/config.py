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

    class Config:
        env_file = ".env"

settings = Settings()