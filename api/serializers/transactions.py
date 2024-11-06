from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional


class GetTransactionInfo(BaseModel):
    transactionid: str = Field(max_length=100)
    transactiontime: int = Field()
    referencenumber: str = Field(max_length=100)
    amount: int
    content: str = Field(max_length=2000)
    bankaccount: str = Field(max_length=100)
    transType: Optional[str] = Field(max_length=100)
    valueDate: Optional[int]
    va: Optional[str] = Field(max_length=100)
    reciprocalBankCode: Optional[str] = Field(max_length=100)
    reciprocalAccount: Optional[str] = Field(max_length=100)
