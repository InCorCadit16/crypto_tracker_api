from fastapi import APIRouter, Query

from typing import Annotated

from markets.schemas import PriceResponse
from markets.api.base import Exchanges
from markets.service import get_prices

router = APIRouter()

@router.get('/prices')
async def fetch_price(left: str, right: str, exchanges: Annotated[list[Exchanges] | None, Query()] = None) -> PriceResponse:
    return await get_prices(left, right, exchanges)
