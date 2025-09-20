# AioQuiqy

Async Python wrapper for the Quiqy payment API. This library provides a simple and intuitive interface for integrating Quiqy payments into your Python applications.

## Features

- 🚀 **Async/Await Support**: Built with `aiohttp` for high-performance async operations
- 📝 **Type Safety**: Full type hints and Pydantic models for request/response validation
- 🔧 **Easy Integration**: Simple API that mirrors the Quiqy REST API
- 📊 **Payment Lifecycle**: Complete support for all payment statuses and callbacks
- 🛡️ **Error Handling**: Comprehensive error handling with detailed error messages
- 🔗 **Webhook Support**: Built-in webhook handler for payment status updates

## Installation

```bash
pip install aioquiqy
```

Or using Poetry:

```bash
poetry add aioquiqy
```

## Quick Start

### Basic Usage

```python
import asyncio
from aioquiqy import AioQuiqy, CreatePaymentRequest, FiatCurrencies

async def main():
    # Initialize the client
    client = AioQuiqy(api_key="your_api_key_here")
    
    # Create a payment
    payment_data = CreatePaymentRequest(
        amount_fiat=100.0,
        callback_url="https://your-site.com/callback",
        client_order_id="order_123",
        fiat_currency_id=FiatCurrencies.USD,
        success_url="https://your-site.com/success",
        fail_url="https://your-site.com/fail"
    )
    
    payment = await client.create_payment(payment_data)
    print(f"Payment created: {payment.id}")
    print(f"Payment URL: https://pay.quiqy.io/{payment.id}")
    
    # Get payment details
    payment_details = await client.get_payment(payment.id)
    print(f"Available crypto currencies: {payment_details.available_crypto_currency_ids}")
    
    # Pre-calculate payment for specific crypto
    calculation = await client.pre_calculate_payment(payment.id, 1)  # TRX
    print(f"Amount to pay: {calculation.payer_amount_crypto} TRX")
    
    # Detail the payment (select crypto currency)
    from aioquiqy.models.payment import DetailPaymentRequest
    detail_data = DetailPaymentRequest(crypto_currency_id=1)  # TRX
    detailed_payment = await client.detail_payment(payment.id, detail_data)
    print(f"Payment detailed: {detailed_payment.payment.status}")
    
    await client.close()

asyncio.run(main())
```

### Webhook Handling

```python
from aioquiqy import AioQuiqy
from aioquiqy.models.payment import CallbackRequest
from aiohttp import web

app = web.Application()
client = AioQuiqy(api_key="your_api_key_here")

@client.callback_handler
async def handle_payment_callback(callback: CallbackRequest, app):
    """Handle payment status updates"""
    print(f"Payment {callback.client_order_id} status: {callback.payment_status}")
    
    if callback.payment_status == "confirmed":
        print("Payment confirmed! Processing order...")
        # Process your order here
    elif callback.payment_status in ["undetailed", "undetected", "unconfirmed"]:
        print("Payment failed or expired")
        # Handle failed payment

# Add webhook route
app.router.add_post('/callback', client.handle_callback)

if __name__ == '__main__':
    web.run_app(app, host='0.0.0.0', port=8080)
```

### Using with aiohttp Web Server

```python
from aiohttp import web
from aioquiqy import AioQuiqy, CreatePaymentRequest, FiatCurrencies

app = web.Application()
client = AioQuiqy(api_key="your_api_key_here")

async def create_payment_handler(request):
    """Create a new payment"""
    data = await request.json()
    
    payment_data = CreatePaymentRequest(
        amount_fiat=data['amount'],
        callback_url="https://your-site.com/callback",
        client_order_id=data['order_id'],
        fiat_currency_id=FiatCurrencies.USD
    )
    
    payment = await client.create_payment(payment_data)
    
    return web.json_response({
        'payment_id': payment.id,
        'payment_url': f"https://pay.quiqy.io/{payment.id}",
        'status': payment.status
    })

app.router.add_post('/create-payment', create_payment_handler)
app.router.add_post('/callback', client.handle_callback)

if __name__ == '__main__':
    web.run_app(app)
```

## API Reference

### Client Methods

#### `create_payment(payment_data: CreatePaymentRequest) -> CreatePaymentResponse`
Create a new payment in detailing state.

#### `get_payment(payment_id: str) -> GetPaymentResponse`
Get full information about a payment.

#### `pre_calculate_payment(payment_id: str, crypto_currency_id: int) -> PreCalculatePaymentResponse`
Calculate payer amount for a specific crypto currency.

#### `detail_payment(payment_id: str, detail_data: DetailPaymentRequest) -> DetailPaymentResponse`
Select crypto currency and move payment to pending state.

### Constants

#### Fiat Currencies
- `FiatCurrencies.USD` (1)
- `FiatCurrencies.EUR` (2) 
- `FiatCurrencies.RUB` (3)

#### Crypto Currencies
- `CryptoCurrencies.TRX` (1)
- `CryptoCurrencies.USDT_TRC20` (2)
- `CryptoCurrencies.ETH` (3)
- `CryptoCurrencies.USDT_ERC20` (4)
- `CryptoCurrencies.BTC` (5)
- `CryptoCurrencies.TON` (6)

#### Payment Status
- `PaymentStatus.DETAILING` - Payment created, crypto not selected
- `PaymentStatus.PENDING` - Crypto selected, waiting for payment
- `PaymentStatus.DETECTED` - Payment detected in blockchain
- `PaymentStatus.CONFIRMED` - Payment confirmed
- `PaymentStatus.UNDETAILED` - Payment expired without crypto selection
- `PaymentStatus.UNDETECTED` - Payment not detected in blockchain
- `PaymentStatus.UNCONFIRMED` - Payment detected but block removed

## Payment Lifecycle

1. **Create Payment** - Payment starts in `detailing` state
2. **Select Crypto** - Use `detail_payment()` to select crypto currency
3. **Payment Pending** - Payment moves to `pending` state
4. **Payment Detection** - Payment moves to `detected` when found in blockchain
5. **Payment Confirmation** - Payment moves to `confirmed` when confirmed

You'll receive callbacks for each status change at your `callback_url`.

## Error Handling

The library raises `QuiqyAPIError` exceptions for API errors:

```python
from aioquiqy.exceptions import QuiqyAPIError

try:
    payment = await client.create_payment(payment_data)
except QuiqyAPIError as e:
    print(f"API Error: {e}")
    print(f"Code: {e.code}")
    print(f"Message: {e.name}")
    print(f"Hint: {e.hint}")
```

## Development

### Setup

```bash
git clone https://github.com/your-username/aioquiqy.git
cd aioquiqy
poetry install
```

### Running Tests

```bash
poetry run pytest
```

### Code Formatting

```bash
poetry run black aioquiqy/
poetry run isort aioquiqy/
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

For support, please open an issue on GitHub or contact the maintainers.