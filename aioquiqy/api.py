from .base import BaseClient
from .const import (
    HTTPMethods,
    Networks,
    # FiatCurrencies,
    # CryptoCurrencies,
    # PaymentStatus,
)

from .models.payment import (
    CreatePaymentRequest,
    CreatePaymentResponse,
    GetPaymentResponse,
    DetailPaymentRequest,
    DetailPaymentResponse,
    PreCalculatePaymentResponse,
    CallbackRequest,
    # CallbackResponse,
)

from typing import Union, List, Callable, Any, Coroutine
from aiohttp.web import Response  # type: ignore[import]
from aiohttp.web_request import Request  # type: ignore[import]


class AioQuiqy(BaseClient):
    """
    Quiqy API client.
        Consists of API methods only.
        All other methods are hidden in the BaseClient.
    """

    API_DOCS = "https://external-api.quiqy.io/docs/doc.json"

    def __init__(
        self, api_key: str, network: Union[str, Networks] = Networks.MAIN_NET
    ) -> None:
        super().__init__()
        """
        Init Quiqy API client
            :param api_key: Your API key from Quiqy settings
            :param network: Network address (default: main net)
        """
        self.__api_key = api_key
        self.network = network
        self.__headers = {"Api-Key": api_key}
        self._handlers: List[
            Callable[[CallbackRequest, Any], Coroutine[Any, Any, Any]]
        ] = []

    async def create_payment(
        self, payment_data: CreatePaymentRequest
    ) -> CreatePaymentResponse:
        """
        Create payment in detailing state.
        https://external-api.quiqy.io/docs/doc.json#operation/createPayment

        Args:
            payment_data: Payment creation data

        Returns:
            CreatePaymentResponse: Created payment details
        """
        method = HTTPMethods.POST
        url = f"{self.network}/payment"

        response = await self._make_request(
            method=method,
            url=url,
            json=payment_data.model_dump(),
            headers=self.__headers,
        )
        return CreatePaymentResponse(**response)

    async def get_payment(self, payment_id: str) -> GetPaymentResponse:
        """
        Get full information about a certain payment.
        https://external-api.quiqy.io/docs/doc.json#operation/getPayment

        Args:
            payment_id: Payment ID in Quiqy service

        Returns:
            GetPaymentResponse: Payment details with available crypto currencies
        """
        method = HTTPMethods.GET
        url = f"{self.network}/payment/{payment_id}"

        response = await self._make_request(
            method=method,
            url=url,
            headers=self.__headers,
        )
        return GetPaymentResponse(**response)

    async def pre_calculate_payment(
        self, payment_id: str, crypto_currency_id: int
    ) -> PreCalculatePaymentResponse:
        """
        Calculate payer amount by rate between selected crypto currency and fiat currency.
        https://external-api.quiqy.io/docs/doc.json#operation/preCalculatePayment

        Args:
            payment_id: Payment ID in Quiqy service
            crypto_currency_id: ID of the selected crypto currency

        Returns:
            PreCalculatePaymentResponse: Calculated payment details
        """
        method = HTTPMethods.GET
        url = f"{self.network}/payment/{payment_id}/calculation"

        params = {"to_crypto_currency_id": crypto_currency_id}

        response = await self._make_request(
            method=method,
            url=url,
            params=params,
            headers=self.__headers,
        )
        return PreCalculatePaymentResponse(**response)

    async def detail_payment(
        self, payment_id: str, detail_data: DetailPaymentRequest
    ) -> DetailPaymentResponse:
        """
        Change payment status to pending by selecting crypto currency.
        https://external-api.quiqy.io/docs/doc.json#operation/detailPayment

        Args:
            payment_id: Payment ID in Quiqy service
            detail_data: Crypto currency selection data

        Returns:
            DetailPaymentResponse: Updated payment details
        """
        method = HTTPMethods.POST
        url = f"{self.network}/payment/{payment_id}/detail"

        response = await self._make_request(
            method=method,
            url=url,
            json=detail_data.model_dump(),
            headers=self.__headers,
        )
        return DetailPaymentResponse(**response)

    def check_callback_signature(self, body_text: str, signature: str) -> bool:
        """
        Verify callback signature (if implemented by Quiqy).
        Note: This method is a placeholder as Quiqy API documentation doesn't specify signature verification.

        Args:
            body_text: Callback request body
            signature: Signature header (if any)

        Returns:
            bool: Whether signature is valid
        """
        # Placeholder implementation - Quiqy API doesn't specify signature verification
        # You may need to implement this based on actual Quiqy requirements
        return True

    async def handle_callback(self, request: Request) -> Response:
        """
        Webhook callback handler for payment status updates.

        Args:
            request: Webhook request

        Returns:
            Response: 200 status code for Quiqy API
        """
        body = await request.json()
        # body_text = await request.text()

        # Parse callback data
        callback_data = CallbackRequest(**body)

        # Process callback with registered handlers
        for handler in self._handlers:
            await handler(callback_data, request.app)

        return Response(text="OK", status=200)

    def register_callback_handler(
        self, func: Callable[[CallbackRequest, Any], Coroutine[Any, Any, Any]]
    ) -> None:
        """
        Register handler for payment status callbacks.

        Args:
            func: Handler function that receives CallbackRequest and app
        """
        self._handlers.append(func)

    def callback_handler(
        self,
        func: Callable[[CallbackRequest, Any], Coroutine[Any, Any, Any]],
    ) -> Callable[[CallbackRequest, Any], Coroutine[Any, Any, Any]]:
        """
        Decorator for registering callback handlers.

        Args:
            func: Handler function

        Returns:
            Decorated function
        """
        self._handlers.append(func)
        return func

    async def __aenter__(self) -> "AioQuiqy":
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any) -> None:
        await self.close()
