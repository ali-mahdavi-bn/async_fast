from pydantic import BaseModel


class RegisterRequestModel(BaseModel):
    first_name: str
    last_name: str
    username: str
    mobile: str
    email: str
    type: int
    is_active: bool
    # username: str
    # password: str
