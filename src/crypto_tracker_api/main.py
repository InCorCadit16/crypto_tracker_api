from fastapi import FastAPI

app = FastAPI()

@app.get("/accounts")
async def get_accounts():
    return {
        'accountsCount': 0,
        'accounts': []
    }
