from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from msg import msg_router
import uvicorn

app = FastAPI()

origins = ["http://127.0.0.1:5501", "http://18.207.12.132:8082", "http://13.54.130.133"]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

@app.get("/") #루트 경로 0.0.0.0:8000/어쩌구
async def welcome() -> dict:
    return {
        "msg" : "fastapi connected"
    }

app.include_router(msg_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=80, reload=True)
