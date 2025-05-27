import uvicorn
from fastapi import FastAPI

from crypto_tracker_api.routers import markets

app = FastAPI()

app.include_router(markets.router, prefix='/market', tags=['Market data'])

if __name__ == '__main__':
    uvicorn.run("main:app", host='0.0.0.0', port=8000, reload=True)
