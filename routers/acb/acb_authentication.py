from fastapi import status
from services.acb.acb_authentication import get_acb_token
from common.responses import APIResponseCode
from views import acb_router


@acb_router.post("/get_token", tags=['ACB'], status_code=status.HTTP_200_OK)
async def get_acb_token_router():
    result = get_acb_token()
    access_token = result.get('access_token')
    try:
        if access_token is not None:
            return {'response': APIResponseCode.SUCCESS, 'result': result}
        else:
            return {'response': APIResponseCode.EXT_API_ERROR, 'message': result.get('error')}
    except Exception as e:
        return {'response': APIResponseCode.SERVER_ERROR, 'error': e}
