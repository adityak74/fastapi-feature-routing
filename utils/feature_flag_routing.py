"""FEature Flag Routing"""

from functools import wraps
from fastapi import HTTPException

FEATURE_FLAGS = {
    "my_feature_flag": True,
}

FEATURE_FLAGS_COMPLEX = {
    "my_feature_flag": {
        "my_platform_1": True,
        "my_platform_2": False,
        "my_platform_3": list()
    }
}


def retrieve_feature_flag(platform):
    return FEATURE_FLAGS_COMPLEX.get("my_feature_flag").get(platform, False)


def validate_flag_name(flag_name, resolver=None):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            if resolver is not None and not callable(resolver):
                raise HTTPException(status_code=500, detail="Feature Flag resolver is not callable")
            if resolver:
                should_follow_feature = resolver(flag_name)
            else:
                should_follow_feature = FEATURE_FLAGS.get(flag_name)
            if not isinstance(should_follow_feature, bool):
                raise HTTPException(status_code=500, detail="Resolver should return a bool")
            if not should_follow_feature:
                raise HTTPException(status_code=400, detail="Feature not enabled.")
            if not isinstance(flag_name, str):
                raise HTTPException(status_code=400, detail="Flag name must be a string")
            return func(*args, **kwargs)
        return wrapper
    return decorator
