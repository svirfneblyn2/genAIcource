from dataclasses import dataclass

@dataclass(frozen=True)
class Order:
    subtotal: float
    country: str
    is_vip: bool = False


def shipping_cost(order: Order) -> float:
    """Return shipping in USD for the current production policy."""
    if order.subtotal < 0:
        raise ValueError("subtotal must be non-negative")
    if order.subtotal >= 100:
        return 0.0
    if order.country.upper() == "US":
        return 7.50
    return 18.00
