from typing import Optional

from backbone.service_layer.general_types import Command


class RegisterCommand(Command):
    first_name: Optional[str]
    last_name: Optional[str]
    username: str
    mobile: int
    email: str
    password: str


class LoginCommand(Command):
    mobile: str
    otp_code: str
    step: int
