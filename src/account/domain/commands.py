from backbone.service_layer.general_types import Command


class RegisterCommand(Command):
    first_name: str
    last_name: str
    username: str
    mobile: str
    email: str
    type: int
    is_active: bool
    # username: str
    # password: str
