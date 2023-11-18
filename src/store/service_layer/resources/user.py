from typing import Dict

from account.domain.entities import UserEntity
from backbone.apis.abstract_api_resource import AbstractApiResource


class UserResource(AbstractApiResource):
    def make(self, model: UserEntity, **kwargs) -> Dict:

        return self.json(
            name=model.name
        )
