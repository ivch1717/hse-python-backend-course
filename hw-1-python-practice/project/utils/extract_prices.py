from typing import Any


def extract_prices(products: list[Any]) -> list[float]:
    return [p.price for p in products]
