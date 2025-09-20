from strenum import StrEnum
from typing import List


class HTTPMethods(StrEnum):
    """Available HTTP methods."""

    POST = "POST"
    GET = "GET"


class Networks(StrEnum):
    """Quiqy networks"""

    MAIN_NET = "https://external-api.quiqy.io"


class FiatCurrencies:
    """Quiqy fiat currencies"""

    USD = 1
    EUR = 2
    RUB = 3

    @classmethod
    def values(cls) -> List[int]:
        """Get all fiat currency IDs"""
        return [cls.USD, cls.EUR, cls.RUB]


class CryptoCurrencies:
    """Quiqy crypto currencies"""

    TRX = 1
    USDT_TRC20 = 2
    ETH = 3
    USDT_ERC20 = 4
    BTC = 5
    TON = 6

    PAYMENT_SUPPORTED = [TRX, USDT_TRC20, ETH, USDT_ERC20, BTC]

    CALLBACK_SUPPORTED = [TRX, USDT_TRC20, ETH, USDT_ERC20, BTC, TON]

    @classmethod
    def payment_supported(cls) -> List[int]:
        """Get crypto currency IDs supported for payment operations"""
        return cls.PAYMENT_SUPPORTED

    @classmethod
    def callback_supported(cls) -> List[int]:
        """Get crypto currency IDs supported for callbacks"""
        return cls.CALLBACK_SUPPORTED


class PaymentStatus(StrEnum):
    """Payment status"""

    DETAILING = "detailing"
    PENDING = "pending"
    DETECTED = "detected"
    CONFIRMED = "confirmed"
    UNDETAILED = "undetailed"
    UNDETECTED = "undetected"
    UNCONFIRMED = "unconfirmed"


class PaymentType(StrEnum):
    """Payment type"""

    FORM = "form"


class FeeToggle(StrEnum):
    """Fee toggle"""

    MERCHANT = "merchant"
    PAYER = "payer"


class FeeSide(StrEnum):
    """Fee side"""

    MERCHANT = "merchant"
    PAYER = "payer"
