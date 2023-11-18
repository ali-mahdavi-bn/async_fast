from tokenize import Name
from typing import Optional

from backbone.service_layer.general_types import Event


class UserCreated(Event):
    mobile: str
    name: Optional[Name] = None
    email: str = None