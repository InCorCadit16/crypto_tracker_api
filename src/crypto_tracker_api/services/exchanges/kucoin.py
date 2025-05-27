from crypto_tracker_api.services.exchanges.base import BaseExchangeApi, Exchanges


class KuCoinApi(BaseExchangeApi):
    EXCHANGE = Exchanges.KUCOIN
    BASE_URL = 'https://api.kucoin.com/api/v1/'
    TICKER_SEPARATOR = '-'

    async def _get_price_for_ticker(self, ticker: str) -> float | None:
        response = await self._make_request('market/orderbook/level1', {'symbol': ticker})
        return float(response['data']['price']) if response.get('data') else None
