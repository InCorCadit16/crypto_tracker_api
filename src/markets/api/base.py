from enum import Enum

import httpx
from typing import Any

from markets.api import ExchangeMeta

class Exchanges(Enum):
    BINANCE = 'binance'
    BYBIT = 'bybit'
    OKX = 'okx'
    KRAKEN = 'kraken'
    COINBASE = 'coinbase'
    KUCOIN = 'kucoin'


class BaseExchangeApi(metaclass=ExchangeMeta):
    """Base class for all exchange API implementations."""
    EXCHANGE = None
    BASE_URL: str = None
    TICKER_SEPARATOR: str = ''

    async def _get_price_for_ticker(self, ticker: str) -> float | None:
        """
        Get the current price for a given ticker.
        
        Args:
            ticker: Trading pair ticker (e.g., 'BTCUSDT')
            
        Returns:
            float: Current price of the trading pair
            
        Raises:
            ValueError: If the price cannot be fetched
        """
        raise NotImplementedError

    async def get_price(self, left: str, right: str) -> float | None:
        """Get current price for given symbols pair"""
        return await self._get_price_for_ticker(f'{left}{self.TICKER_SEPARATOR}{right}'.upper())

    async def _make_request(self, endpoint: str, params: dict[str, Any] = None) -> dict:
        """
        Make an HTTP request to the exchange API.
        
        Args:
            endpoint: API endpoint to call
            params: Query parameters for the request
            
        Returns:
            Dict: JSON response from the API
            
        Raises:
            ValueError: If the request fails
        """
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{self.BASE_URL}{endpoint}", params=params)
            if response.status_code != 200:
                raise ValueError(f"API request failed with status {response.status_code}")
            return response.json()
