# -*- coding: utf-8 -*-
from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime, Boolean, BigInteger
from .base_model import BaseModel


class Transaction(BaseModel):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    transaction_id = Column(String(100), unique=True, nullable=False)
    transaction_time = Column(BigInteger, nullable=False)
    reference_number = Column(String(100), nullable=False)
    amount = Column(Integer, nullable=False)
    content = Column(String(500), nullable=False)
    bank_account = Column(String(100), nullable=False)
    trans_type = Column(String(100), nullable=True)
    value_date = Column(BigInteger, nullable=True)
    va = Column(String(100), nullable=True)
    reciprocal_account = Column(String(100), nullable=True)
    reciprocal_bank_code = Column(String(100), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    is_deleted = Column(Boolean, default=False)
