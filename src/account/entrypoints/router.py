from fastapi import APIRouter
from redis.asyncio import Redis

from account.domain.commands import RegisterCommand
from account.entrypoints.request_model import RegisterRequestModel
from account.service_layer.usecase.get_user import get_user
from account.service_layer.usecase.register_user import register_user
from unit_of_work import UnitOfWork

# from unit_of_work import UnitOfWork

router = APIRouter(prefix="/account", tags=["account"])


@router.get("/a")
async def root():
    # redis_host: str = "redis"
    # redis_port: int = "6379"
    # redis_db: int = 0
    # r = await Redis(host=redis_host, port=redis_port, db=redis_db, decode_responses=True, retry_on_timeout=True)
    # await r.set("a", "ali")
    # print("========================")
    # print(await r.get("a"))
    # print("========================")
    # return register_user(uow=UnitOfWork())
    uow = UnitOfWork()
    async with uow:
        user = await uow.user.find_by_id(38)
        print(user.normalize_dict())


@router.post("/b")
async def register(request_model: RegisterRequestModel):
    command = RegisterCommand(**request_model.model_dump())
    return await register_user(command=command)
    # return {"a": "a"}
    # return await get_user()
