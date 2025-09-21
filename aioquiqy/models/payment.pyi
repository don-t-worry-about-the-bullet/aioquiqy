from pydantic import BaseModel, Field, field_validator
from typing import Optional, List
from datetime import datetime
from ..const import (
    FiatCurrencies,
    PaymentStatus,
    PaymentType,
    CryptoCurrencies,
)

class CreatePaymentRequest(BaseModel):
    amount_fiat: float
    callback_url: str
    client_order_id: str
    fail_url: Optional[str]
    fiat_currency_id: int
    success_url: Optional[str]
    
    @field_validator("fiat_currency_id")
    @classmethod
    def validate_fiat_currency_id(cls, v: int) -> int: ...

class PaymentResponse(BaseModel):
    amount_crypto: Optional[float]
    amount_fiat: float
    callback_url: Optional[str]
    client_order_id: str
    confirmed_manually: bool
    created_at: datetime
    crypto_currency_id: Optional[int]
    fail_url: Optional[str]
    fee: Optional[float]
    fee_toggle: Optional[str]
    fiat_currency_id: int
    from_address: Optional[str]
    id: str
    payer_amount_crypto: Optional[float]
    status: PaymentStatus
    success_url: Optional[str]
    to_address: Optional[str]
    ttl: int
    tx_hash: Optional[str]
    type: PaymentType
    updated_at: datetime

class CreatePaymentResponse(BaseModel):
    amount_crypto: Optional[float]
    amount_fiat: float
    callback_url: Optional[str]
    client_order_id: str
    confirmed_manually: bool
    created_at: datetime
    crypto_currency_id: Optional[int]
    fail_url: Optional[str]
    fee: Optional[float]
    fee_toggle: Optional[str]
    fiat_currency_id: int
    from_address: Optional[str]
    id: str
    payer_amount_crypto: Optional[float]
    status: PaymentStatus
    success_url: Optional[str]
    to_address: Optional[str]
    ttl: int
    tx_hash: Optional[str]
    type: PaymentType
    updated_at: datetime

class GetPaymentResponse(BaseModel):
    available_crypto_currency_ids: List[int]
    payment: PaymentResponse

class DetailPaymentRequest(BaseModel):
    crypto_currency_id: int
    
    @field_validator("crypto_currency_id")
    @classmethod
    def validate_crypto_currency_id(cls, v: int) -> int: ...

class DetailPaymentResponse(BaseModel):
    available_crypto_currency_ids: List[int]
    payment: PaymentResponse

class PreCalculatePaymentResponse(BaseModel):
    amount_crypto: float
    crypto_currency_id: int
    fee: float
    fee_toggle: str
    payer_amount_crypto: float
    
    @field_validator("crypto_currency_id")
    @classmethod
    def validate_crypto_currency_id(cls, v: int) -> int: ...

class CallbackRequest(BaseModel):
    amount_crypto: Optional[float]
    amount_fiat: float
    client_order_id: str
    crypto_currency_id: Optional[int]
    fee_crypto: Optional[float]
    fee_fiat: Optional[float]
    fee_side: Optional[str]
    fiat_currency_id: int
    from_address: Optional[str]
    payer_amount_crypto: Optional[float]
    payment_created_at: datetime
    payment_status: PaymentStatus
    payment_status_updated_at: Optional[datetime]
    planned_expiration_at: datetime
    to_address: Optional[str]
    tx_hash: Optional[str]
    
    @field_validator("fiat_currency_id")
    @classmethod
    def validate_fiat_currency_id(cls, v: int) -> int: ...
    
    @field_validator("crypto_currency_id")
    @classmethod
    def validate_crypto_currency_id(cls, v: Optional[int]) -> Optional[int]: ...

class CallbackResponse(BaseModel):
    class Config:
        extra: str
