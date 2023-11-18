from __future__ import annotations

from enum import Enum
from typing import List

from pydantic import BaseModel


class BaseEnumeration(Enum):
    @classmethod
    def members(cls) -> List[BaseEnumeration]:
        return [item[1] for item in cls.__members__.items()]

    @classmethod
    def find_by_value(cls, value) -> BaseEnumeration:
        for item in cls.members():
            if value == item.value:
                return item


class Command(BaseModel):
    pass


class Event(BaseModel):
    pass
