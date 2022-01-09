from typing import Optional

from pydantic import BaseSettings


class EnvSettings(BaseSettings):
    SQL_DSN: Optional[str] = "sqlite:///db.sqlite3"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
