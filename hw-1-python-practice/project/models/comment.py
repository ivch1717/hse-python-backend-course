from __future__ import annotations

from datetime import datetime
from uuid import UUID


class Comment:
    def __init__(self, author_id: UUID, text: str) -> None:
        self.author_id: UUID = author_id
        self.text: str = text
        self.create_data: datetime = datetime.now()
        self.update_data: datetime = self.create_data
        self.like_count: int = 0

    def edit_comment(self, new_text: str) -> None:
        self.text = new_text
        self.update_data = datetime.now()

    def like(self) -> None:
        self.like_count += 1

    def dislike(self) -> None:
        self.like_count -= 1

    def __repr__(self) -> str:
        return f"Comment(author_id={self.author_id}, likes={self.like_count}, text='{self.text}')"
