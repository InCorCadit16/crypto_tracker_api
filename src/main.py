from fastapi import FastAPI
from fastapi.params import Depends

from dependencies import user_dependency
from markets.router import router as markets_router
from auth.router import router as auth_router

app = FastAPI()

app.include_router(auth_router, prefix='/auth', tags=['Authentication'])
app.include_router(markets_router, prefix='/markets', tags=['Markets data'], dependencies=[Depends(user_dependency)])
