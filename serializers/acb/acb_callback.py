from pydantic import BaseModel


class AuthCallbackData(BaseModel):
    auth_code: str
    user_id: str
