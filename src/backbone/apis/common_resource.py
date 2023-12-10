from typing import Any, Dict, List

from starlette.responses import JSONResponse

from backbone.adapter.abstract_entity import BaseEntity
from backbone.apis.abstract_api_resource import AbstractApiResource


class BaseCommandResource(AbstractApiResource):
    def make(self, model: Any, message="", lang="fa") -> Dict:
        data = None
        if isinstance(model, dict):
            data = model
        elif isinstance(model, BaseEntity):
            if hasattr(model, "uuid"):
                _uuid = model.uuid
                data = {"uuid": _uuid}
            elif hasattr(model, "id"):
                _uuid = model.id
                data = {"id": _uuid}
        else:
            data = model
        return self.json(
            message=message,
            data={"data": data},
        )


def default_message(*, message, data = {}, status=200):
    return JSONResponse(content={
        "message": message,
        "data": data
    }, status_code=status)
