from fastapi import FastAPI

from crypto_tracker_api.routers import prices

app = FastAPI()

app.include_router(prices.router, prefix='/prices', tags=['Prices'])
