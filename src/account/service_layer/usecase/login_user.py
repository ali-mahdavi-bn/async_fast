from sqlalchemy import Text
from starlette.responses import JSONResponse

from account.domain import commands
from account.service_layer.resources.user import UserResource
from backbone.apis.common_resource import default_message
from backbone.apis.translator.translatore import translate
from backbone.configs import config
from backbone.helpers.utils import generateOTP
from backbone.infrastructure.databases.redis.connection import RedisConnection
from backbone.service_layer.general_types import Command
from backbone.services.auth import create_access_token, get_current_user, decode, generate_access_token
from unit_of_work import UnitOfWork


async def login_user(*, command: commands.LoginCommand
                     , uow=UnitOfWork):
    """Login user.

       Retrieves the user from the unit of work based on the provided command.
       If the user does not exist, returns a default message indicating that the mobile number is not valid.
       If the command step is 1, generates an OTP code, stores it in Redis, and returns a default message indicating that the OTP has been sent.
       If the command step is 2, retrieves the OTP code from Redis and compares it with the provided OTP code.
       If the OTP codes match, generates an access token and returns a default message indicating a successful login.

       Args:
           command (commands.LoginCommand): The login command containing the mobile number and OTP code.
           uow (UnitOfWork): The unit of work.

       Returns:
           JSONResponse: The response containing the message and data.

       """
    async with uow() as uow:
        user = await uow.user.find_by_mobile(command.mobile)
        print(user)
        if not user:
            return default_message(message=translate(phrase='otp.valid.mobile', type='message'), data={
                'has_account': False
            }, status=200)

    if command.step == 1:
        async with RedisConnection() as r:
            if await r.exists(command.mobile):
                return default_message(message=translate(phrase='otp.send.already', type='message'), data={
                    'has_account': True,
                    'current_step': 1,
                    'next_step': 2,
                    'ttl': await r.ttl(command.mobile)
                }, status=200)

            otp_code = generateOTP()
            print(otp_code)
            await r.set_value(command.mobile, otp_code, exp=config.EXPIRE_OTP_CODE)
            return default_message(message=translate(phrase='otp.send', type='message'), data={
                'has_account': True,
                'current_step': 2,
                'next_step': 3,
                'ttl': await r.ttl(command.mobile)
            })

    elif command.step == 2:
        async with RedisConnection() as r:
            get_otp_code = await r.get_value(command.mobile)
            if not get_otp_code:
                return default_message(message=translate(phrase='otp.expire', type='message'), data={
                    'has_account': True,
                    'current_step': 2,
                    'next_step': 1
                })

            if get_otp_code != command.otp_code:
                return default_message(message=translate(phrase='otp.valid.code', type='message'), data={
                    'has_account': True,
                    'current_step': 2,
                    'next_step': 2
                })

            token = await generate_access_token(command.mobile)
            return default_message(message=translate(phrase='login.success', type='message'), data={
                'token': token,
                'has_account': True,
                'current_step': 2,
                'next_step': 3
            })
