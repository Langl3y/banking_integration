from fastapi import status
from typing import Optional
from requests import Request

from serializers.acb import AuthCallbackData
from views import acb_router


@acb_router.get('/authentication/callback')
async def get_callback_code(data: AuthCallbackData):
    auth_code = data.auth_code
    user_id = data.user_id

    return {"auth_code": auth_code, "user_id": user_id}
