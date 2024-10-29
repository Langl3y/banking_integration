from pydantic import BaseModel
from typing import List, Optional


# Define the Virtual Account Info model
class VirtualAccountInfo(BaseModel):
    vaPrefixCd: Optional[str] = None
    vaNbr: Optional[str] = None


# Define the Transaction Entity Attribute model
class TransactionEntityAttribute(BaseModel):
    traceNumber: Optional[str] = None
    beneficiaryName: Optional[str] = None
    beneficiaryAccountNumber: Optional[str] = None
    receiverBankName: Optional[str] = None
    remitterName: Optional[str] = None
    remitterAccountNumber: Optional[str] = None
    issuerBankName: Optional[str] = None
    virtualAccount: Optional[str] = None
    referenceNumber: Optional[str] = None
    partnerCustomerCode: Optional[str] = None
    partnerCustomerName: Optional[str] = None
    partnerCustomerType: Optional[str] = None


# Define the Transaction model
class Transaction(BaseModel):
    transactionStatus: str
    transactionChannel: str  # Allowed values could be validated further
    transactionCode: str
    accountNumber: str
    transactionDate: str
    effectiveDate: str
    debitOrCredit: str
    virtualAccountInfo: Optional[VirtualAccountInfo] = None
    amount: int
    transactionEntityAttribute: Optional[TransactionEntityAttribute] = None
    transactionContent: str


# Define the Pagination model
class Pagination(BaseModel):
    page: int
    pageSize: int
    totalPages: int


# Define the Request Meta model
class RequestMeta(BaseModel):
    requestType: str
    requestCode: str


# Define the Request Params model
class RequestParams(BaseModel):
    transactions: List[Transaction]
    pagination: Pagination


# Define the Request model
class Request(BaseModel):
    requestMeta: RequestMeta
    requestParams: RequestParams


# Define the Master Meta model
class MasterMeta(BaseModel):
    clientId: str
    clientRequestId: str


# Define the ACB Notification Serializer model
class ACBNotificationSerializer(BaseModel):
    masterMeta: MasterMeta
    requests: List[Request]
