from fastapi import APIRouter, Query

from typing import Annotated

from crypto_tracker_api.schemas.markets import PriceResponse
from crypto_tracker_api.services.exchanges.base import Exchanges
from crypto_tracker_api.services.markets import get_prices

router = APIRouter()

@router.get('/prices', response_model=PriceResponse)
async def fetch_price(left: str, right: str, exchanges: Annotated[list[Exchanges] | None, Query()] = None):
    return await get_prices(left, right, exchanges)
