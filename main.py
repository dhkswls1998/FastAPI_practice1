# main.py

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app.database.sqlite import engine
from app.routers import router_user
from app.routers import router_xxx

app = FastAPI()

# CORS 설정 : local test -> 주석처리 변경
origins = ["null"]
# origins = ["http://192.168.74.31:8080"]
# origins = ["http://localhost:8080"]
# origins = ["http://59.5.235.142:8080"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def add_cors_header(request: Request, call_next):
    response = await call_next(request)
    response.headers["Access-Control-Allow-Origin"] = "null"
    response.headers["Access-Control-Allow-Headers"] = "*"
    return response

from app.database.crud_user import Base as UserBase

UserBase.metadata.create_all(bind=engine)

app.include_router(router_user.router)
app.include_router(router_xxx.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)