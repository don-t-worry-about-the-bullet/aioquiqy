from strenum import StrEnum
from typing import List


class HTTPMethods(StrEnum):
    """Available HTTP methods."""

    POST = "POST"
    GET = "GET"


class Networks(StrEnum):
    """Quiqy networks"""

    MAIN_NET = "https://external-api.quiqy.io"


class FiatCurrencies(StrEnum):
    """Quiqy fiat currencies"""

    USD = "1"
    EUR = "2"
    RUB = "3"

    @classmethod
    def values(cls) -> List[str]:
        return [currency.value for currency in cls]


class CryptoCurrencies(StrEnum):
    """Quiqy crypto currencies"""

    TRX = "1"
    USDT_TRC20 = "2"
    ETH = "3"
    USDT_ERC20 = "4"
    BTC = "5"
    TON = "6"

    @classmethod
    def values(cls) -> List[str]:
        return [currency.value for currency in cls]


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

