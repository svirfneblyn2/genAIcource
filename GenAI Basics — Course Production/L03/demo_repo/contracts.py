from typing import Literal
from pydantic import BaseModel, Field


class SupportTicket(BaseModel):
    category: Literal["bug", "question", "feature"]
    priority: Literal["low", "medium", "high"]
    summary: str = Field(min_length=1, max_length=160)
    needs_human_review: bool
