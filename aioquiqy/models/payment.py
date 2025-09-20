from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

from ..const import (
    # FiatCurrencies,
    # CryptoCurrencies,
    PaymentStatus,
    PaymentType,
    # FeeToggle,
    # FeeSide,
)


class CreatePaymentRequest(BaseModel):
    """Request model for creating a payment"""
    
    amount_fiat: float = Field(..., description="Amount in fiat currency")
    callback_url: str = Field(..., description="URL to receive payment callbacks")
    client_order_id: str = Field(..., description="Unique order ID in your service")
    fail_url: Optional[str] = Field(None, description="URL to redirect on payment failure")
    fiat_currency_id: int = Field(..., description="Fiat currency ID (1=USD, 2=EUR, 3=RUB)")
    success_url: Optional[str] = Field(None, description="URL to redirect on payment success")


class PaymentResponse(BaseModel):
    """Payment response model"""
    
    amount_crypto: Optional[float] = Field(None, description="Amount in crypto currency")
    amount_fiat: float = Field(..., description="Amount in fiat currency")
    callback_url: Optional[str] = Field(None, description="Callback URL")
    client_order_id: str = Field(..., description="Client order ID")
    confirmed_manually: bool = Field(..., description="Whether payment was confirmed manually")
    created_at: datetime = Field(..., description="Payment creation timestamp")
    crypto_currency_id: Optional[int] = Field(None, description="Crypto currency ID")
    fail_url: Optional[str] = Field(None, description="Failure redirect URL")
    fee: Optional[float] = Field(None, description="Fee amount")
    fee_toggle: Optional[str] = Field(None, description="Fee toggle (merchant/payer)")
    fiat_currency_id: int = Field(..., description="Fiat currency ID")
    from_address: Optional[str] = Field(None, description="Sender address")
    id: str = Field(..., description="Payment ID")
    payer_amount_crypto: Optional[float] = Field(None, description="Amount payer needs to send")
    status: PaymentStatus = Field(..., description="Payment status")
    success_url: Optional[str] = Field(None, description="Success redirect URL")
    to_address: Optional[str] = Field(None, description="Recipient address")
    ttl: int = Field(..., description="Time to live in seconds")
    tx_hash: Optional[str] = Field(None, description="Transaction hash")
    type: PaymentType = Field(..., description="Payment type")
    updated_at: datetime = Field(..., description="Last update timestamp")


class CreatePaymentResponse(BaseModel):
    """Response model for creating a payment"""
    
    amount_crypto: Optional[float] = None
    amount_fiat: float
    callback_url: Optional[str] = None
    client_order_id: str
    confirmed_manually: bool
    created_at: datetime
    crypto_currency_id: Optional[int] = None
    fail_url: Optional[str] = None
    fee: Optional[float] = None
    fee_toggle: Optional[str] = None
    fiat_currency_id: int
    from_address: Optional[str] = None
    id: str
    payer_amount_crypto: Optional[float] = None
    status: PaymentStatus
    success_url: Optional[str] = None
    to_address: Optional[str] = None
    ttl: int
    tx_hash: Optional[str] = None
    type: PaymentType
    updated_at: datetime


class GetPaymentResponse(BaseModel):
    """Response model for getting payment details"""
    
    available_crypto_currency_ids: List[int] = Field(..., description="Available crypto currency IDs")
    payment: PaymentResponse = Field(..., description="Payment details")


class DetailPaymentRequest(BaseModel):
    """Request model for detailing a payment"""
    
    crypto_currency_id: int = Field(..., description="Crypto currency ID to use for payment")


class DetailPaymentResponse(BaseModel):
    """Response model for detailing a payment"""
    
    available_crypto_currency_ids: List[int] = Field(..., description="Available crypto currency IDs")
    payment: PaymentResponse = Field(..., description="Updated payment details")


class PreCalculatePaymentResponse(BaseModel):
    """Response model for payment pre-calculation"""
    
    amount_crypto: float = Field(..., description="Amount in crypto currency")
    crypto_currency_id: int = Field(..., description="Crypto currency ID")
    fee: float = Field(..., description="Fee amount")
    fee_toggle: str = Field(..., description="Fee toggle (merchant/payer)")
    payer_amount_crypto: float = Field(..., description="Amount payer needs to send")


class CallbackRequest(BaseModel):
    """Callback request model"""
    
    amount_crypto: Optional[float] = Field(None, description="Amount in crypto currency")
    amount_fiat: float = Field(..., description="Amount in fiat currency")
    client_order_id: str = Field(..., description="Client order ID")
    crypto_currency_id: Optional[int] = Field(None, description="Crypto currency ID")
    fee_crypto: Optional[float] = Field(None, description="Fee in crypto")
    fee_fiat: Optional[float] = Field(None, description="Fee in fiat")
    fee_side: Optional[str] = Field(None, description="Fee side (merchant/payer)")
    fiat_currency_id: int = Field(..., description="Fiat currency ID")
    from_address: Optional[str] = Field(None, description="Sender address")
    payer_amount_crypto: Optional[float] = Field(None, description="Amount payer needs to send")
    payment_created_at: datetime = Field(..., description="Payment creation timestamp")
    payment_status: PaymentStatus = Field(..., description="Current payment status")
    payment_status_updated_at: Optional[datetime] = Field(None, description="Status update timestamp")
    planned_expiration_at: datetime = Field(..., description="Planned expiration timestamp")
    to_address: Optional[str] = Field(None, description="Recipient address")
    tx_hash: Optional[str] = Field(None, description="Transaction hash")


class CallbackResponse(BaseModel):
    """Callback response model - can contain any JSON fields"""
    
    class Config:
        extra = "allow"

