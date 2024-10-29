from fastapi import status, Query
from typing import Optional
from requests import Request

from common.responses import APIResponseCode
from views import acb_router


@acb_router.get('/authentication')
async def get_callback_code(auth_code: str = Query(...), user_id: str = Query(...)):
    result = {"auth_code": auth_code, "user_id": user_id}
    try:
        return {'response': APIResponseCode.SUCCESS, 'result': result}
    except Exception as e:
        return {'response': APIResponseCode.SERVER_ERROR, 'error': e}
