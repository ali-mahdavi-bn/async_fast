from backbone.service_layer.general_types import Command


class RegisterUser(Command):
    mobile: str
    otp: str
