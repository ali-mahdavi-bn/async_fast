from datetime import timedelta

from fastapi import APIRouter, HTTPException, Depends
from redis.asyncio import Redis
import re

from account.domain import commands
from account.entrypoints import request_model
from account.service_layer.usecase.get_user import get_user
from account.service_layer.usecase.login_user import login_user
from account.service_layer.usecase.register_user import register_user
from backbone.apis.common_resource import default_message
from backbone.infrastructure.databases.redis.connection import RedisConnection
from unit_of_work import UnitOfWork

# from unit_of_work import UnitOfWork

router = APIRouter(prefix="/account", tags=["account"])

from starlette.requests import Request

from backbone.exception import UnauthorizedException, BadRequestException


async def current_user(request: Request):
    # print(request.state.user)
    pass
    # if request.state.user is None:
    #     raise UnauthorizedException()
    # return request.state.user


@router.get("/a")
async def root(user=Depends(current_user)):
    # redis_host: str = "redis"
    # redis_port: int = "6379"
    # redis_db: int = 0
    # r = await Redis(host=redis_host, port=redis_port, db=redis_db, decode_responses=True, retry_on_timeout=True)
    # await r.set("a", "ali")
    # print("========================")
    # print(await r.get("a"))
    # print("========================")
    # return register_user(uow=UnitOfWork())
    # raise HTTPException(status_code=403, detail="is not login")
    # print(await user)

    # function to generate OTP
    a = re.match(r"^(0)?9\d{9}$", '+989901541408') is not None

    # Driver code
    # print("OTP of 4 digits:")

    async with RedisConnection() as r:
        a = await r.get_value('a')
        print(a)


@router.post("/register")
async def register(request_model: request_model.RegisterRequestModel):
    """Register a user.

    Creates a register command using the provided request model and calls the register_user function with the command.

    Args:
        request_model: The request model containing the data for user registration.

    Returns:
        The result of the register_user function.

    """

    command = commands.RegisterCommand(**request_model.model_dump())

    return await register_user(command=command)


@router.post("/login/")
async def login(request_model: request_model.LoginRequestModel, step: int):
    """Login a user.

    Creates a login command using the provided request model and step, and calls the login_user function with the command.

    Args:
        request_model: The request model containing the data for user login.
        step: The step of the login process.

    Returns:
        The result of the login_user function.

    """

    command = commands.LoginCommand(**request_model.model_dump(), step=step)
    return await login_user(command=command)
    # print(step)
