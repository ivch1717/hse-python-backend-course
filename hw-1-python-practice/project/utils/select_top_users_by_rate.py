from typing import Any


def select_top_users_by_rate(users: list[Any], top_size: int) -> list[Any]:
    return sorted(users, key=lambda u: u.rate, reverse=True)[:top_size]
