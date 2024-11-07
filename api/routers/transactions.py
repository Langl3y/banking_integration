from fastapi import APIRouter, Depends
from typing import Optional

from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from api.common.utils import *
from api.serializers import GetTransactionInfo
from api.services import TransactionService
from api.common.responses import APIResponseCode
from api.common.utils import get_db

transactions_router = APIRouter(prefix='', tags=['Transactions'])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/tokenUrl")


@transactions_router.post('/transaction-sync', response_model=dict)
async def transaction_sync(access_token: str = Depends(oauth2_scheme), data_body: Optional[GetTransactionInfo] = None,
                           db: Session = Depends(get_db)):
    try:
        payload = decode_jwt(access_token)
        if payload.get('exp') >= datetime.utcnow().timestamp():
            transaction_service = TransactionService(db)
            result = transaction_service.transaction_sync(data_body)

            return {
                'error': False,
                'errorReason': APIResponseCode.SUCCESS.get('code'),
                'toastMessage': '',
                'object': {
                    'reftransactionid': result.__dict__.get('id'),
                }
            }
        return {
            'error': True,
            'errorReason': APIResponseCode.NO_PERMISSION.get('code'),
            'toastMessage': APIResponseCode.NO_PERMISSION.get('message'),
        }
    except Exception as e:
        return {
            'error': True,
            'errorReason': APIResponseCode.ALREADY_EXISTS.get('code'),
            'toastMessage': APIResponseCode.ALREADY_EXISTS.get('message')
        }
