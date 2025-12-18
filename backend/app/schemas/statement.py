from pydantic import BaseModel
from typing import Optional


class StatementResponse(BaseModel):
    bank: str

    outstanding_amount: Optional[str]
    minimum_due: Optional[str]
    due_date: Optional[str]

    interest_rate: str
    late_fee: str

    transaction_count: int
    top_spending_category: str
