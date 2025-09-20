from typing import Union


def calculate_crypto_amount(fiat_amount: float, rate: float) -> float:
    """
    Calculate crypto amount from fiat amount using exchange rate.
    
    Args:
        fiat_amount: Amount in fiat currency
        rate: Exchange rate (crypto per fiat)
        
    Returns:
        float: Amount in crypto currency
    """
    return fiat_amount * rate


def calculate_fiat_amount(crypto_amount: float, rate: float) -> float:
    """
    Calculate fiat amount from crypto amount using exchange rate.
    
    Args:
        crypto_amount: Amount in crypto currency
        rate: Exchange rate (fiat per crypto)
        
    Returns:
        float: Amount in fiat currency
    """
    return crypto_amount * rate


def get_payment_url(payment_id: str) -> str:
    """
    Get payment form URL for a given payment ID.
    
    Args:
        payment_id: Payment ID
        
    Returns:
        str: Payment form URL
    """
    return f"https://pay.quiqy.io/{payment_id}"


def format_currency_amount(amount: Union[int, float], currency: str) -> str:
    """
    Format currency amount with appropriate decimal places.
    
    Args:
        amount: Amount to format
        currency: Currency code
        
    Returns:
        str: Formatted amount string
    """
    if currency.upper() in ['BTC', 'ETH']:
        return f"{amount:.8f} {currency}"
    elif currency.upper() in ['USDT', 'USDC']:
        return f"{amount:.2f} {currency}"
    else:
        return f"{amount:.6f} {currency}"

