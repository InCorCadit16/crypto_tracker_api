from markets.api.base import BaseExchangeApi, Exchanges


class CoinbaseApi(BaseExchangeApi):
    EXCHANGE = Exchanges.COINBASE
    BASE_URL = 'https://api.coinbase.com/v2/'
    TICKER_SEPARATOR = '-'

    async def _get_price_for_ticker(self, ticker: str) -> float | None:
        response = await self._make_request(f'prices/{ticker}/spot')
        return float(response['data']['amount']) if response.get('data') else None
