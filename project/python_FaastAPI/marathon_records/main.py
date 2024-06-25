from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

# frontend 빌드를 통해 서비스에 필요한 라이브러리
from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles

from domain import router

app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# router파일을 사용
# main에 작성할 수도 있지만 코드가 복잡해질 수 있기에 따로 구성하여 관리
app.include_router(router.router)

app.mount("/assets", StaticFiles(directory="frontend/dist/assets"))

@app.get("/")
def index():
    return FileResponse("frontend/dist/index.html")