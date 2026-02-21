import os

from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

SECRET_HEADER = "SECRET"
SECRET_VALUE = os.getenv("HEADER_SECRET")


class HeaderSecretChecker(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        header_value = request.headers.get(SECRET_HEADER)
        if header_value != SECRET_VALUE:
            return JSONResponse(status_code=403, content={"detail": "Forbidden"})

        response = await call_next(request)
        return response
