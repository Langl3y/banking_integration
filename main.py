import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from routers.acb import acb_router

load_dotenv()

allowed_hosts = os.getenv('ALLOWED_HOSTS')
app = FastAPI()
app.add_middleware(TrustedHostMiddleware, allowed_hosts=allowed_hosts)

app.include_router(acb_router)


@app.get("/")
def api_list():
    return {"message": "Banking Integration Gateway - ver 1.0"}
