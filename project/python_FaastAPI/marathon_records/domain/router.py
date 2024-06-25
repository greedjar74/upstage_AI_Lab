# 특정 domain에 대한 수행 역할을 부여
# crud파일의 각 함수를 실행하여 특정 기능이 수행 됨

from fastapi import APIRouter, Depends # Depends를 통해 의존성 부여
from sqlalchemy.orm import Session

from database import get_db
from domain import schema, crud

router = APIRouter(prefix='')

# 메인 화면
@router.get('/records', response_model=list[schema.record])
def records(db: Session=Depends(get_db)):
    _records = crud.get_records(db) # crud의 함수를 통해 기록 리스트를 가져온다.
    return _records

# 특정 기록 가져오기
@router.get('/record_detail/{id}', response_model=schema.record)
def get_record_detail(id, db: Session=Depends(get_db)):
    _record_detail = crud.get_record_detail(db, id=id)
    return _record_detail

# 기록 입력
# 유저에게 입력을 받는다. -> post사용
# 입력 데이터 형태 : dict형태로 데이터를 가져와서 각각의 데이터를 추출해서 사용해야된다. -> javascript의 특성
# data는 입력값을 의미하고 dict형태이다. -> data = {'marathon':'~', 'date'='~', ... , dnf='~'}
@router.post('/update_record')
def update_record(new_record:dict, db: Session=Depends(get_db)): # schema를 통해 미리 설정한 데이터 형태에 부합하는지 확인
    crud.update_record(db=db,marathon=new_record["marathon"], date=new_record["date"], bibnum=new_record["bibnum"], record=new_record["record"], dnf=new_record["dnf"])

# 기록 수정
# id를 통해 특정 데이터를 가져오고 객체를 수정한다.
# 입력 데이터 형태 : dict형태로 데이터를 가져와서 각각의 데이터를 추출해서 사용해야된다. -> javascript의 특성
@router.post('/modify_record')
def modify_record(new_data:dict, db: Session=Depends(get_db)):
    crud.modify_record(db=db, id=new_data['id'], col=new_data['col'], data=new_data['data'])

# 특정 기록 삭제
# id를 통해 특정 데이터를 지정하고 삭제한다.
@router.post('/delete_record')
def delete_record(id:dict, db: Session=Depends(get_db)):
    print(id)
    crud.delete_record(db=db, id=id)

# 전체 데이터 삭제
# 사용자로부터 특정 문장을 입력 받아야 삭제될 수 있게 한다.
# 입력 데이터가 없으므로 get으로 처리
@router.get('/delete_all')
def delete_all(db:Session=Depends(get_db)):
    # if delete_text == 'delete all': -> frontend에서 처리
    crud.delete_all(db=db) 
