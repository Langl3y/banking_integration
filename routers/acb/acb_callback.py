from fastapi import status, Query
from typing import Optional
from requests import Request

from views import acb_router


@acb_router.get('/authentication')
async def get_callback_code(auth_code: str = Query(...), user_id: str = Query(...)):
    print(auth_code)
    return {"auth_code": auth_code, "user_id": user_id}
