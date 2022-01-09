from typing import Optional

from sqlmodel import SQLModel, Field


class UserAuthentication(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, description="ID")
    email: int = Field(index=True, description="User Email")
    hashed_password: str = Field(max_length=512, description="User Password Hashed")
    otp_secret: Optional[str] = Field(default=None, description="TOTP Secret")
