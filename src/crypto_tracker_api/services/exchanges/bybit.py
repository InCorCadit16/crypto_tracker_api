from crypto_tracker_api.services.exchanges.base import BaseExchangeApi, Exchanges


class BybitApi(BaseExchangeApi):
    EXCHANGE = Exchanges.BYBIT
    BASE_URL = 'https://api.bybit.com/v5/'

    async def _get_price_for_ticker(self, ticker: str) -> float | None:
        response = await self._make_request('market/tickers', {'category': 'spot', 'symbol': ticker})
        return float(response['result']['list'][0]['lastPrice']) if response.get('result') else None
