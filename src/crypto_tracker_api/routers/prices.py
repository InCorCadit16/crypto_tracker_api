from fastapi import APIRouter

from crypto_tracker_api.models.price import PriceResponse
from crypto_tracker_api.services.prices import get_price

router = APIRouter()

@router.get('/{symbol}', response_model=PriceResponse)
def fetch_price(symbol: str):
    return get_price(symbol)