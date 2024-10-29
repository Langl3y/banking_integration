# -*- coding: utf-8 -*-
import requests
import urllib3

from common.utils import *

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_acb_token():
    acb_api_token = acb_data.get('acb_api_token')
    data_body = {'grant_type': acb_data['acb_grant_type'],
                 'client_id': acb_data['acb_client_id'],
                 'client_secret': acb_data['acb_client_secret'],
                 }
    try:
        result = requests.post(url=acb_api_token, headers=basic_headers, data=data_body)
    except Exception as e:
        return {'error': str(e)}
    return result.json()
