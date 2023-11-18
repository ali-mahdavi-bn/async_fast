from datetime import datetime
from datetime import timedelta
from typing import Union, Any

import jwt
from fastapi import HTTPException
from passlib.context import CryptContext
from starlette import status

from backbone.infrastructure.databases.redis.connection import RedisConnection
from unit_of_work import UnitOfWork

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
    decoded_token = jwt.decode(token_bytes, JWT_SECRET_KEY, ALGORITHM)
    return decoded_token


class JWTError:
    pass


async def get_current_user(token_u):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        token = token_u.strip()
        payload = decode(token)
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except Exception as e:
        print(e)
        # raise credentials_exception

    uow = UnitOfWork()


    async with RedisConnection() as r:
        a = await r.get_value(token)
        print(a)

    # try:
    #     async with uow:
    #         user = await uow.user.find_by_id(int(user_id))
    # except:
    #     raise credentials_exception




    # return user
