# -*- coding: utf-8 -*-
import requests
import urllib3
import datetime
from common.utils import *
from common.responses import ACBResponseCode

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_acb_transaction_notification(notification):
    try:
        result = {
            "timestamp": datetime.now().isoformat() + "Z",
            "responseCode": ACBResponseCode.SUCCESS['code'],
            "message": ACBResponseCode.SUCCESS['message'],
            "responseBody": {
                "index": 1,
                "referenceCode": notification.masterMeta.clientRequestId
            }
        }
    except Exception as e:
        return {'error': str(e)}
    return result
