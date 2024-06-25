from sqlalchemy import Column, Integer, String, Text, DateTime

from database import Base

class Records(Base):
    __tablename__ = 'records'

    id = Column(Integer, primary_key=True) # 각 데이터의 id
    title = Column(String, nullable=False) # 마라톤 대회 이름
    date = Column(String, nullable=False) # 대회 일시
    bibnum = Column(Integer, nullable=False) # 배번호
    record = Column(String, nullable=True) # 기록
    finish = Column(String, nullable=False) # 완주여부
    create_date = Column(DateTime,nullable=False) # 기록 업로드 일자