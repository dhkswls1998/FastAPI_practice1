# router_xxx.py

from fastapi import APIRouter

router = APIRouter()

@router.get("/hello")
async def get_hello():
    return {"message": "hello"}