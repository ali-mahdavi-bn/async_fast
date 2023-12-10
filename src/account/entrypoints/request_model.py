from typing import Optional

from pydantic import BaseModel


class RegisterRequestModel(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    username: str
    mobile: int
    email: str
    password: str


class LoginRequestModel(BaseModel):
    mobile: str
    otp_code: str
