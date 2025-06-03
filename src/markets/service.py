import asyncio
from markets.schemas import PriceResponse
from markets.api import ExchangeMeta
from markets.api.base import Exchanges


async def get_prices(left: str, right: str, include_exchanges: list[Exchanges] = None) -> PriceResponse:
    exchanges = []
    tasks = []
    for exchange, exchange_api in ExchangeMeta.get_all().items():
        if not include_exchanges or exchange in include_exchanges:
            exchanges.append(exchange)
            tasks.append(exchange_api().get_price(left, right))

    results = await asyncio.gather(*tasks, return_exceptions=True)

    return PriceResponse(
        symbol=f'{left}{right}'.upper(),
        prices={exchange.value: price for exchange, price in zip(exchanges, results)}
    )
