from .base import BaseClient
from .const import HTTPMethods, Networks
from .models.payment import (
    CreatePaymentRequest,
    CreatePaymentResponse,
    GetPaymentResponse,
    DetailPaymentRequest,
    DetailPaymentResponse,
    PreCalculatePaymentResponse,
    CallbackRequest,
)
from typing import Union, List, Callable, Any, Coroutine
from aiohttp.web import Response
from aiohttp.web_request import Request

class AioQuiqy(BaseClient):
    API_DOCS: str
    network: Union[str, Networks]
    _handlers: List[Callable[[CallbackRequest, Any], Coroutine[Any, Any, Any]]]
    
    def __init__(
        self, api_key: str, network: Union[str, Networks] = Networks.MAIN_NET
    ) -> None: ...
    
    async def create_payment(
        self, payment_data: CreatePaymentRequest
    ) -> CreatePaymentResponse: ...
    
    async def get_payment(self, payment_id: str) -> GetPaymentResponse: ...
    
    async def pre_calculate_payment(
        self, payment_id: str, crypto_currency_id: int
    ) -> PreCalculatePaymentResponse: ...
    
    async def detail_payment(
        self, payment_id: str, detail_data: DetailPaymentRequest
    ) -> DetailPaymentResponse: ...
    
    def check_callback_signature(self, body_text: str, signature: str) -> bool: ...
    
    async def handle_callback(self, request: Request) -> Response: ...
    
    def register_callback_handler(
        self, func: Callable[[CallbackRequest, Any], Coroutine[Any, Any, Any]]
    ) -> None: ...
    
    def callback_handler(
        self,
        func: Callable[[CallbackRequest, Any], Coroutine[Any, Any, Any]],
    ) -> Callable[[CallbackRequest, Any], Coroutine[Any, Any, Any]]: ...
    
    async def __aenter__(self) -> "AioQuiqy": ...
    
    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any) -> None: ...
