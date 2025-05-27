import httpx

from crypto_tracker_api.models.price import PriceResponse

BINANCE_URL = 'https://api.binance.com/api/v3/'


def get_price(symbol: str) -> PriceResponse:
    return PriceResponse(symbol=symbol, prices={
        'binance': _get_price_binance(symbol)
    })

def _get_price_binance(symbol: str):
    response = httpx.get(f'{BINANCE_URL}ticker/price?symbol={symbol}')
    if response.status_code != 200:
        raise ValueError(f'Could not fetch price for {symbol}')
    return float(response.json()['price'])
