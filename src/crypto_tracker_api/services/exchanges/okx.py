from crypto_tracker_api.services.exchanges.base import BaseExchangeApi, Exchanges


class OkxApi(BaseExchangeApi):
    EXCHANGE = Exchanges.OKX
    BASE_URL = 'https://www.okx.com/api/v5/'
    TICKER_SEPARATOR = '-'

    async def _get_price_for_ticker(self, ticker: str) -> float | None:
        response = await self._make_request('market/ticker', {'instId': ticker})
        return float(response['data'][0]['last']) if response.get('data') else None
