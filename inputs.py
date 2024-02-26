from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class Invoice(BaseModel):
    amount: int
    name: str
    tax_id: str
    due: datetime
    expiration: datetime
    fine: float
    interest: float
    tags: list
    rules: Optional[list]

class Transaction(BaseModel):
    amount: int
    receiver_id: str
    description: str
    external_id: str
    tags: list

    