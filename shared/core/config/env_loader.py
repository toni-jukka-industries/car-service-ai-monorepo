import os
from dotenv import load_dotenv
from pydantic import BaseSettings, ValidationError

# Load environment variables from a .env file
load_dotenv()

class Settings(BaseSettings):
    APP_NAME: str = "Car Service AI OS"
    ENVIRONMENT: str = "development"  # could be 'production' or 'development'
    LOG_LEVEL: str = "info"
    DATABASE_URL: str
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"

    class Config:
        env_file = ".env"

try:
    settings = Settings()
except ValidationError as e:
    print("Configuration error:", e)
    raise

__all__ = ["settings"]