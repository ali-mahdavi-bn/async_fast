from fastapi import APIRouter

from account.bootstrap import bootstrap
from account.domain import commands
from account.entrypoints.request_model import RegisterRequestModel

router = APIRouter(prefix="/account", tags=["account"])
bus = bootstrap()


@router.post("/aasdad")
async def rooot(request_model: RegisterRequestModel):
    cmd = commands.RegisterUser(**request_model.dict())
    return bus.handle(cmd)
