from fastapi import APIRouter

from account.entrypoints.request_model import RegisterRequestModel
from account.service_layer.usecase import register_user
from unit_of_work import UnitOfWork

router = APIRouter(prefix="/account", tags=["account"])



@router.get("/a")
async def rooot():
    return register_user(uow=UnitOfWork())
    # return {"a":"b"}
