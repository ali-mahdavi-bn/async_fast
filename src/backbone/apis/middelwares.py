from fastapi import HTTPException
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response, JSONResponse

from backbone.configs import config
from backbone.services.auth import get_current_user, decode
from unit_of_work import UnitOfWork


class AuthenticateMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        try:

            header = request.headers.get('Authorization')
            request.state.user = None
            request.state.token = None

            if header is None:
                raise ValueError("is not login")
            protocol, _, token = header.partition(" ")

            if token == config.TOKEN_VALID:
                return await call_next(request)

            elif token:
                a = str(token)
                user = await get_current_user(a)
                request.state.user = user
                request.state.token = token

            return await call_next(request)
        except Exception as e:
            return JSONResponse(content=str(e), status_code=403, headers={"WWW-Authenticate": "Bearer"})
