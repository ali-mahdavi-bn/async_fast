from pydantic import BaseModel


class RegisterRequestModel(BaseModel):
    mobile: str
    otp: str
