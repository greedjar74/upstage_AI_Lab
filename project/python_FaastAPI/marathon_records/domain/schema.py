# db에서 데이터를 가져올 때 각각의 데이터에 대한 형식을 지정해준다.
# 가져오는 데이터가 해당 형식을 잘 갖추고 있는지 검사

from pydantic import BaseModel

# 기록 데이터에 대한 정의
class record(BaseModel):
    id: int
    marathon: str
    date: str
    bibnum: int
    record: str
    dnf: str

    # 버전에 따라 해당 부분이 없으면 오류가 발생
    class Config:
        orm_mode = True