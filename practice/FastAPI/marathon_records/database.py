# import contextlib # 의존성 주입 -> Depends를 사용하기에 더이상 사용 안 함

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'sqlite:///./records.db' # 데이터베이스 이름

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# 의존성 주입 -> 매번 세션을 열고 반환하는 과정을 작성할 필요가 없다.
# @contextlib.contextmanager -> Depends를 사용하여 제거해줘야 된다.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()