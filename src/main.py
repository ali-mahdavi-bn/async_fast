from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request

# routes
from account.entrypoints.router import router as account_router
from backbone.apis.middelwares import AuthenticateMiddleware
# mappers
from backbone.infrastructure.databases.postgres_connection import DEFAULT_ENGIN, Base
from account.adapters.data_models import *
from enumeration.adapters.data_models import *
from store.adapters.data_models import *
from product.adapters.data_models import *


@asynccontextmanager
async def lifespan(app: FastAPI):
    # redis_host: str = config.REDIS_HOST
    # redis_port: int = config.REDIS_PORT
    # redis_db: int = 0
    # r = await Redis(host=redis_host, port=redis_port, db=redis_db, decode_responses=True, retry_on_timeout=True)

    # migrate_enumerations(DEFAULT_SESSION_FACTORY)
    async with DEFAULT_ENGIN.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    # Base.metadata.create_all(DEFAULT_ENGIN)
    # MAPPER_REGISTRY.configure()
    yield
    # clear_mappers()


app = FastAPI(lifespan=lifespan)


app.add_middleware(AuthenticateMiddleware)




origins = [
    "http://localhost",
    "http://localhost:8080",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(account_router)
if __name__ == "__main__":
    import uvicorn

    uvicorn.run('main:app', host="0.0.0.0", port=8000, reload=True)
