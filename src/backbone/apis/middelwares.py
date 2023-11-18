from fastapi import HTTPException
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response

from backbone.services.auth import get_current_user, decode
from unit_of_work import UnitOfWork


class AuthenticateMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        header = request.headers.get('Authorization')
        request.state.user = None
        request.state.token = None

        if header is None:
            raise HTTPException(status_code=403, detail="is not login")
        protocol, _, token = header.partition(" ")

        if token:
            user = await get_current_user(token)
            request.state.user = user
            request.state.token = token

        return await call_next(request)
