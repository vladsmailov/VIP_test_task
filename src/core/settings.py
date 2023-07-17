import os
from pathlib import Path

from pydantic import BaseSettings

BASE_DIR = Path(__file__).resolve().parent.parent.parent
if os.path.exists(str(BASE_DIR / ".env")):
    ENV_FILE = ".env"


class Settings(BaseSettings):
    """Настройки проекта."""

    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    DB_HOST: str
    DB_PORT: str
