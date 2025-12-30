from typing import Any


def get_ordered_comments_by_likes(comments: list[Any]) -> list[Any]:
    return sorted(comments, key=lambda c: c.like_count, reverse=True)
