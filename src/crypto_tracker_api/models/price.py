from pydantic import BaseModel


class PriceResponse(BaseModel):
    symbol: str
    prices: dict[str, float]
