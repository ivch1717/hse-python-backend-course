from typing import Any


def get_ordered_products_by_price(products: list[Any]) -> list[Any]:
    return sorted(products, key=lambda p: p.price, reverse=True)
