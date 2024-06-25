from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from domain import router # router 객체를 FastAPI 앱에 등록

app = FastAPI()

origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router.router) # main app에 router 등록