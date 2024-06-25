import datetime

from pydantic import BaseModel

# 데이터를 주고받을 때 지켜야 되는 양식을 지정하는 것
class Records(BaseModel):
    id: int
    title: str
    date: str
    bibnum: int
    record: str
    finish: str
    create_date: datetime.datetime

    # 버전에 따라 적어줘야됨 -> 나는 이거 적어야 제대로 작동
    class Config:
        orm_mode = True