from account.domain.entities import UserEntity
from backbone.apis.abstract_api_resource import AbstractApiResource


class UserResource(AbstractApiResource):
    def make(self, model: UserEntity, **kwargs):
        return self.json(
            id=model.id,
            uuid=model.uuid,
            first_name=model.first_name,
            last_name=model.last_name,
            username=model.username,
            type=model.type,
            email=model.email,
            mobile=model.mobile,
            created_at=model.created_at,
            updated_at=model.updated_at,
            deleted_at=model.deleted_at,
        )
