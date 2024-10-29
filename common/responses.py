class APIResponseCode(object):
    FAILURE = {"code": -1, "message": 'General failure'}  # General logic error
    SUCCESS = {"code": 0, "message": 'Success'}  # Successful response
    SERVER_ERROR = {"code": 1, "message": 'Server error'}  # Unexpected error during handling the request
    BAD_REQUEST = {"code": 2, "message": 'Bad request'}  # Error returned by DRF serializer
    NO_PERMISSION = {"code": 3, "message": 'No permission'}  # Error related to permissions
    NOT_FOUND = {"code": 4, "message": 'Not found'}  # Object not found
    ALREADY_EXISTS = {"code": 5, "message": 'Already exists'}  # Object already exists
    VALIDATION_ERROR = {"code": 6, "message": 'Validation error'}  # Error related to invalidated input
    INVALID_ACTION = {"code": 7, "message": 'Invalid request'}  # Invalid action (stateful)
    ACTION_DENIED = {"code": 8, "message": 'Action denied'}  # Invalid action (stateless)
    FILE_ERROR = {"code": 9, "message": 'File error'}  # Error related to file handling
    DB_ERROR = {"code": 10, "message": 'Database error'}  # Error related to database
    EXT_API_ERROR = {"code": 11, "message": 'External API error'}  # Error related to calling external API
    TIMEOUT = {"code": 12, "message": 'Request timed out'}  # Timeout when handling a request
    EXPIRED = {"code": 13, "message": 'Request expired'}
    TOO_MANY_REQUEST = {"code": 14, "message": 'Too many request'}

    @classmethod
    def is_success(cls, code):
        return code == cls.SUCCESS

    @classmethod
    def is_failure(cls, code):
        return code != cls.SUCCESS


class ACBResponseCode(object):
    SUCCESS = {"code": '00000000', "message": 'Request was successfully processed'}
    INVALID_TOKEN = {"code": '00000001', "message": 'Invalid token'}
    WRONG_API = {"code": '00000002', "message": 'Wrong API function'}
    MISSING_FIELDS = {"code": '00000003', "message": 'Missing required parameters'}
    WRONG_PAYMENT_CHANNEL_CODE = {"code": '00000004', "message": 'Wrong payment Channel code'}
    WRONG_REQUEST_KEY_TYPE = {"code": '00000005', "message": 'Wrong Request Key type'}
    SYSTEM_ERROR = {"code": '00000099', "message": 'System error'}
    INVALID_POLICY_NUMBER = {"code": '00000101', "message": 'Invalid policy number'}
    INVALID_APPLICATION_NUMBER = {"code": '00000104', "message": 'Invalid application number'}
    POLICY_NOT_SUITABLE_FOR_PREMIUM_COLLECTION = {"code": '00000103', "message": 'Policy is not suitable for premium collection'}
    INVALID_REQUEST_CODE = {"code": '00000201', "message": 'Invalid requestCode'}
    INVALID_REQUEST_KEY = {"code": '00000202', "message": 'Invalid requestKey'}
    INVALID_PAYMENT_TYPE_CODE = {"code": '00000203', "message": 'Invalid paymentTypeCode'}
    INVALID_PAYMENT_METHOD_CODE = {"code": '00000204', "message": 'Invalid paymentMethodCode'}
    INVALID_TRANSACTION_AMOUNT = {"code": '00000205', "message": 'Invalid transactionAmount'}
    DUPLICATE_TRANSACTION_REFERENCE_CODE = {"code": '00000206', "message": 'Duplicate transactionReferenceCode'}
    INVALID_CARD_TYPE = {"code": '00000207', "message": 'Invalid cardType'}
    INVALID_RELATIONSHIP_WITH_PO = {"code": '00000208', "message": 'Invalid relationshipWithPo'}
    INVALID_DATETIME_FORMAT = {"code": '00000209', "message": 'Invalid datetime format'}
    INVALID_TRANSACTION_CHANNEL = {"code": '00000211', "message": 'Invalid transaction channel'}
    INVALID_TRANSACTION_REFERENCE_CODE = {"code": '00000301', "message": 'Invalid transactionReferenceCode'}
    OVER_CUT_OFF_TIME_FOR_VOIDING_TRANSACTION = {"code": '00000302', "message": 'Over cut-off time for voiding transaction'}
    TRANSACTION_IS_RECONCILIATED = {"code": '00000303', "message": 'Transaction is reconciliated'}
    NOT_MATCH_TRANSACTIONS = {"code": '00000401', "message": 'Not match transactions'}

    @staticmethod
    def get_response(response_code):
        response_mapping = {
            "00000000": (200, ACBResponseCode.SUCCESS),
            "00000001": (401, ACBResponseCode.INVALID_TOKEN),
            "00000002": (404, ACBResponseCode.WRONG_API),
            "00000003": (400, ACBResponseCode.MISSING_FIELDS),
            "00000004": (400, ACBResponseCode.WRONG_PAYMENT_CHANNEL_CODE),
            "00000005": (400, ACBResponseCode.WRONG_REQUEST_KEY_TYPE),
            "00000099": (500, ACBResponseCode.SYSTEM_ERROR),
            "00000101": (400, ACBResponseCode.INVALID_POLICY_NUMBER),
            "00000104": (400, ACBResponseCode.INVALID_APPLICATION_NUMBER),
            "00000103": (400, ACBResponseCode.POLICY_NOT_SUITABLE_FOR_PREMIUM_COLLECTION),
            "00000201": (400, ACBResponseCode.INVALID_REQUEST_CODE),
            "00000202": (400, ACBResponseCode.INVALID_REQUEST_KEY),
            "00000203": (400, ACBResponseCode.INVALID_PAYMENT_TYPE_CODE),
            "00000204": (400, ACBResponseCode.INVALID_PAYMENT_METHOD_CODE),
            "00000205": (400, ACBResponseCode.INVALID_TRANSACTION_AMOUNT),
            "00000206": (400, ACBResponseCode.DUPLICATE_TRANSACTION_REFERENCE_CODE),
            "00000207": (400, ACBResponseCode.INVALID_CARD_TYPE),
            "00000208": (400, ACBResponseCode.INVALID_RELATIONSHIP_WITH_PO),
            "00000209": (400, ACBResponseCode.INVALID_DATETIME_FORMAT),
            "00000211": (400, ACBResponseCode.INVALID_TRANSACTION_CHANNEL),
            "00000301": (400, ACBResponseCode.INVALID_TRANSACTION_REFERENCE_CODE),
            "00000302": (400, ACBResponseCode.OVER_CUT_OFF_TIME_FOR_VOIDING_TRANSACTION),
            "00000303": (400, ACBResponseCode.TRANSACTION_IS_RECONCILIATED),
            "00000401": (400, ACBResponseCode.NOT_MATCH_TRANSACTIONS),
        }
        return response_mapping.get(response_code, (400, {"code": 'unknown', "message": 'Unknown error code'}))