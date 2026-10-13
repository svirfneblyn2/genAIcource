from dataclasses import dataclass


@dataclass(frozen=True)
class Order:
    subtotal: float
    zone: str  # "CITY" or "OUTSIDE"
    is_prime: bool = False


def delivery_fee(order: Order) -> float:
    """Return the delivery fee in USD for the current production rules."""
    if order.subtotal < 0:
        raise ValueError("subtotal must be non-negative")
    if order.subtotal >= 100:
        return 0.0
    if order.zone.upper() == "CITY":
        return 7.50
    return 18.00
