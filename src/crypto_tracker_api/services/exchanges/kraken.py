from crypto_tracker_api.services.exchanges.base import BaseExchangeApi, Exchanges


class KrakenApi(BaseExchangeApi):
    EXCHANGE = Exchanges.KRAKEN
    BASE_URL = 'https://api.kraken.com/0/public/'

    async def _get_price_for_ticker(self, ticker: str) -> float | None:
        response = await self._make_request('Ticker', {'pair': ticker})
        if response.get('result'):
            pair_name = list(response['result'].keys())[0]
            return float(response['result'][pair_name]['c'][0])  # 'c' is the last trade closed price
        return None
