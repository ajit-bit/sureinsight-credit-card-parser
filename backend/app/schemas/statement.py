from pydantic import BaseModel
from typing import Optional

class StatementResponse(BaseModel):
    bank: str

    outstanding_amount: Optional[str] = None
    minimum_due: Optional[str] = None
    due_date: Optional[str] = None

    credit_limit: Optional[str] = None
    available_credit: Optional[str] = None
    used_credit: Optional[str] = None

    reward_points: Optional[str] = None
    statement_issue_date: Optional[str] = None
