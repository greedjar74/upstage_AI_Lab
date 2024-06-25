# 데이터 베이스에 대한 설정

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# DB 접속 url
SQLALCHEMY_DATABASE_URL = 'sqlite:///./records.db' # sqlite의 경우 개발 단계에서 사용하고 개발 완료후 배포할 때 큰 DB로 변경한다.

# sqlalchemy 데이터베이스를 사용하기 위한 규칙
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}) # 커넥션 풀 생성 : 데이터베이스에 접속하느 객체를 일정 갯수만큼 만들고 돌려가며 사용
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # autocommit=True인 경우 자동으로 db에 데이터가 올라간다 -> 데이터 소실 문제가 발생할 수 있음

Base = declarative_base()

# db의존성 부여 -> 매번 닫아주는 코드 작성 필요없음
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()