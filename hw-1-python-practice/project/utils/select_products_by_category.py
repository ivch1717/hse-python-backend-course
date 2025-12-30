from typing import Any


def select_products_by_category(products: list[Any], category: str) -> list[Any]:
    return [p for p in products if p.category == category]
