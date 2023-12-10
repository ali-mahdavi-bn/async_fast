from datetime import datetime
from datetime import timedelta
from typing import Union, Any

import jwt
from fastapi import HTTPException
from jwt import ExpiredSignatureError
from passlib.context import CryptContext
from starlette import status
from starlette.responses import JSONResponse

from backbone.infrastructure.databases.redis.connection import RedisConnection
from unit_of_work import UnitOfWork


def credentials_exception(message: str = 'Could not validate credentials'):
    return Exception(str(message))


ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 30 minutes
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7  # 7 days
ALGORITHM = "HS256"
JWT_SECRET_KEY = 'JWT_SECRET_KEY'  # should be kept secret
JWT_REFRESH_SECRET_KEY = 'JWT_REFRESH_SECRET_KEY'  # should be kept secret

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_hashed_password(password: str) -> str:
    return password_context.hash(password)


def verify_password(password: str, hashed_pass: str) -> bool:
    return password_context.verify(password, hashed_pass)


def create_access_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    try:
        if expires_delta is not None:
            expires_delta = datetime.utcnow() + expires_delta
        else:
            expires_delta = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

        to_encode = {"exp": expires_delta, "sub": str(subject)}
        encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, ALGORITHM)
        return encoded_jwt
    except Exception as e:
        raise ValueError(f"value error for token!!!  {e}")


def create_refresh_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    try:
        if expires_delta is not None:
            expires_delta = datetime.utcnow() + expires_delta
        else:
            expires_delta = datetime.utcnow() + timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)

        to_encode = {"exp": expires_delta, "sub": str(subject)}
        encoded_jwt = jwt.encode(to_encode, JWT_REFRESH_SECRET_KEY, ALGORITHM)
        return encoded_jwt
    except:
        raise ValueError("value error for refresh_token!!!")


def decode(token: str):
    token_bytes = token.encode('utf-8')  # Convert the token to bytes
    try:
        decoded_token = jwt.decode(token_bytes,
                                   JWT_SECRET_KEY, ALGORITHM)
        return decoded_token
    except ExpiredSignatureError as e:
        raise credentials_exception(e)


async def get_current_user(token_u: str):
    try:
        token = token_u.strip()
        payload = decode(token)
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception()
    except ExpiredSignatureError as e:
        raise credentials_exception(e)

    uow = UnitOfWork()

    async with RedisConnection() as r:
        get_redis_token = await r.get_value(token)

    if get_redis_token:
        try:
            async with uow:
                user = await uow.user.find_by_id(int(user_id))
        except:
            raise credentials_exception()
    else:
        raise credentials_exception()

    return user


async def generate_access_token(subject):
    async with RedisConnection() as r:
        generate_token = create_access_token(subject)
        await r.set_value(generate_token, generate_token)
        print(generate_token)
        return generate_token
