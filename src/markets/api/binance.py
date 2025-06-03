from markets.api.base import BaseExchangeApi, Exchanges


class BinanceApi(BaseExchangeApi):
    EXCHANGE = Exchanges.BINANCE
    BASE_URL = 'https://api.binance.com/api/v3/'

    async def _get_price_for_ticker(self, ticker: str) -> float | None:
        response = await self._make_request('ticker/price', {'symbol': ticker})
        return float(response['price']) if response.get('price') else None
