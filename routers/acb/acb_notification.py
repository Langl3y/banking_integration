import datetime
from fastapi import status
from typing import Optional

from services.acb.acb_notification import get_acb_transaction_notification
from serializers.acb import ACBNotificationSerializer
from views import acb_router


@acb_router.post('/send_notification', status_code=status.HTTP_201_CREATED)
async def send_acb_notification_router(notification: Optional[ACBNotificationSerializer]):
    result = get_acb_transaction_notification(notification)
    print(notification.model_dump())

    return result
