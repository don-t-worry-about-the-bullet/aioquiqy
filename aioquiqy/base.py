import asyncio
import ssl
from typing import Optional, Any, Dict

import certifi
from aiohttp import ClientSession, TCPConnector
from aiohttp.typedefs import StrOrURL

from .exceptions import QuiqyAPIError


class BaseClient:
    """Base aiohttp client"""

    def __init__(self) -> None:
        """
        Set defaults on object init.
            By default `self._session` is None.
            It will be created on a first API request.
            The second request will use the same `self._session`.
        """
        self._loop = asyncio.get_event_loop()
        self._session: Optional[ClientSession] = None

    def get_session(self, **kwargs: Any) -> ClientSession:
        """Get cached session. One session per instance."""
        if isinstance(self._session, ClientSession) and not self._session.closed:
            return self._session

        ssl_context = ssl.create_default_context(cafile=certifi.where())
        connector = TCPConnector(ssl=ssl_context)

        self._session = ClientSession(connector=connector, **kwargs)
        return self._session

    async def _make_request(
        self, method: str, url: StrOrURL, **kwargs: Any
    ) -> Dict[str, Any]:
        """
        Make a request.
            :param method: HTTP Method
            :param url: endpoint link
            :param kwargs: data, params, json and other...
            :return: status and result or exception
        """
        session = self.get_session()

        async with session.request(method, url, **kwargs) as response:
            if response.status >= 400:
                error_data: Dict[str, Any] = await response.json()
                self._handle_error(response.status, error_data)

            response_data = await response.json(content_type="application/json")
        return response_data  # type: ignore

    @staticmethod
    def _handle_error(status_code: int, error_data: Dict[str, Any]) -> None:
        """Handle API errors"""
        hint = error_data.get("hint")
        msg = error_data.get("msg", "Unknown error")
        raise QuiqyAPIError(status_code, msg, hint or "")

    async def close(self) -> None:
        """Close the session graceful."""
        if not isinstance(self._session, ClientSession):
            return

        if self._session.closed:
            return

        await self._session.close()
