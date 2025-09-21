from strenum import StrEnum
from typing import List

class HTTPMethods(StrEnum):
    POST: str
    GET: str

class Networks(StrEnum):
    MAIN_NET: str

class FiatCurrencies:
    USD: int
    EUR: int
    RUB: int
    
    @classmethod
    def values(cls) -> List[int]: ...

class CryptoCurrencies:
    TRX: int
    USDT_TRC20: int
    ETH: int
    USDT_ERC20: int
    BTC: int
    TON: int
    
    PAYMENT_SUPPORTED: List[int]
    CALLBACK_SUPPORTED: List[int]
    
    @classmethod
    def payment_supported(cls) -> List[int]: ...
    
    @classmethod
    def callback_supported(cls) -> List[int]: ...

class PaymentStatus(StrEnum):
    DETAILING: str
    PENDING: str
    DETECTED: str
    CONFIRMED: str
    UNDETAILED: str
    UNDETECTED: str
    UNCONFIRMED: str

class PaymentType(StrEnum):
    FORM: str

class FeeToggle(StrEnum):
    MERCHANT: str
    PAYER: str

class FeeSide(StrEnum):
    MERCHANT: str
    PAYER: str
