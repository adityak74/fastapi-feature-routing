"""Feature Flag Route"""

import asyncio
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from utils.feature_flag_routing import validate_flag_name, retrieve_feature_flag

router = APIRouter()


@router.get("/feature")
@validate_flag_name("my_platform_1", retrieve_feature_flag)
def get_feature():
    return JSONResponse(status_code=200, content={"message": "hello"})


@router.get("/feature_async")
@validate_flag_name("my_platform_1", retrieve_feature_flag)
async def get_feature():
    await asyncio.sleep(1)
    return JSONResponse(status_code=200, content={"message": "hello"})
