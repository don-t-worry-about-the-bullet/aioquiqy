import asyncio
import ssl
from typing import Optional, Any, Dict
from aiohttp import ClientSession, TCPConnector
from aiohttp.typedefs import StrOrURL

class BaseClient:
    _loop: asyncio.AbstractEventLoop
    _session: Optional[ClientSession]
    
    def __init__(self) -> None: ...
    
    def get_session(self, **kwargs: Any) -> ClientSession: ...
    
    async def _make_request(
        self, method: str, url: StrOrURL, **kwargs: Any
    ) -> Dict[str, Any]: ...
    
    @staticmethod
    def _handle_error(status_code: int, error_data: Dict[str, Any]) -> None: ...
    
    async def close(self) -> None: ...
