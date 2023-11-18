import copy
import datetime
from dataclasses import dataclass
from uuid import UUID



class BaseEntity:
    def normalize_dict(self):
        d = {}

        for attr, value in self.__dict__.items():

            if attr in ("events", "_sa_instance_state"):
                continue
            value = value.__str__() if isinstance(value, UUID) else value
            value = value.isoformat() if isinstance(value, datetime.time) or isinstance(value, datetime.date) else value
            value = value.strftime('%Y-%m-%d %H:%M:%S') if isinstance(value, datetime.datetime) else value
            d[attr] = value
        return d


@dataclass
class BaseDTO:
    pass

