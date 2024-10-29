# -*- coding: utf-8 -*-
import os
import re
import hmac
import hashlib

from datetime import datetime, timezone
from dotenv import load_dotenv

load_dotenv()

acb_data = {
    'acb_client_id': os.getenv('ACB_CLIENT_ID'),
    'acb_client_secret': os.getenv('ACB_CLIENT_SECRET'),
    'acb_grant_type': os.getenv('ACB_GRANT_TYPE'),
    'acb_api_token': os.getenv('ACB_API_TOKEN'),
    'acb_api_logout': os.getenv('ACB_API_LOGOUT'),
    'acb_api_notification': os.getenv('ACB_API_NOTIFICATION'),
    'acb_api_credit': os.getenv('ACB_API_CREDIT'),
    'acb_api_debit': os.getenv('ACB_API_DEBIT'),
}

basic_headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/x-www-form-urlencoded',
}
