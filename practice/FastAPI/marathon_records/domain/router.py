from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db # 의존성 주입

from domain import schema, crud

# 기본 주소 설정
router = APIRouter(
    prefix = '/marathon_records'
)

# 모든 기록 리스트 반환 -> main화면
@router.get('/records_list', response_model=list[schema.Records]) # 주소 및 스키마 설정
def records_list(db: Session=Depends(get_db)):
    # db = SessionLocal() # 데이터베이스 세션 생성 -> 의존성 주입으로 매번 열고 반환할 필요가 없다.
    #_records_list = db.query(Records).order_by(Records.create_date.desc()).all() # 리스트 가져오기 -> 라우터 없이
    # db.close() # 데이터베이스 세션을 커넥션 풀에 반환하는 함수 -> 종료하는 것이 아니다.

    _records_list = crud.get_records_list(db)

    return _records_list # 기록 리스트 반환

# 하나의 기록 가져오기
@router.get('/record_detail', response_model=list[schema.Records])
def record_detail(db: Session=Depends(get_db)):
    _record_detail = crud.get_record_detail(db, id=id)
    return _record_detail

# 기록 추가
@router.post('/update_record', response_model=list[schema.Records])
def update_record(new_record: dict, db: Session=Depends(get_db)): # 새로운 기록을 입력받는다. -> dict형태 -> javascript특징
    crud.update_record(db=db, title=new_record['marathon'], date=new_record['date'], bibnum=new_record['bibnum'], record=new_record['record'], finish=new_record['finish'])

# 기록 수정
@router.post('/modify_record')
def modify_record(new_data:dict, db: Session=Depends(get_db)):
    crud.modify_record(db=db, id=new_data['id'], col=new_data['col'], data=new_data['data'])

# 하나의 기록 삭제
@router.post('/delete_record')
def delete_record(id:dict, db: Session=Depends(get_db)):
    crud.delete_record(db=db, id=id)

# 모든 기록 삭제
@router.post('/delete_all_records')
def delete_all_records(db: Session=Depends(get_db)):
    crud.delete_all_records(db=db)