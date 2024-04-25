from fastapi import FastAPI
import uvicorn
from ff_routing_fastapi.routes.feature_flag import router as feature_flag_router

app = FastAPI()
app.include_router(feature_flag_router, prefix="/feature_flag", tags=[""])


if __name__ == "__main__":
    uvicorn.run("main:app")
