from typing import Any


def filter_comments_by_author(comments: list[Any], author: Any) -> list[Any]:
    return [c for c in comments if c.author_id == author.id]
