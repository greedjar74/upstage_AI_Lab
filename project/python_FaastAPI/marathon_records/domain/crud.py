# 각각의 domain에서 수행하는 역할을 함수로 만들어둔다.
# router에서 사용된다.

from models import Records
from sqlalchemy.orm import Session

# 모든 기록을 반환하는 함수 -> 첫 화면에서 사용됨
def get_records(db:Session):
    records = db.query(Records).order_by(Records.id.desc()).all() # asc(): 오름차순으로 불러오기, desc(): 내림차순으로 불러오기
    return records

# 특정 기록을 가져오는 함수
def get_record_detail(db:Session, id):
    record_detail = db.query(Records).get(id)
    return record_detail

# 기록은 db에 추가하는 함수
# new_record 형태 : '대회명_일시_배번호_기록_완주여부'
def update_record(db:Session, marathon, date, bibnum, record, dnf):
    record = Records(marathon=marathon, date=date, bibnum=bibnum, record=record, dnf=dnf)
    db.add(record)
    db.commit()


# db에 있는 데이터 수정
# new_record 형태 : 'id, col, 변환값'
def modify_record(db:Session, id, col, data):
    q = db.query(Records).get(id)
    # 각 col에 맞게 데이터를 정제하여 입력
    if col == 'date':
        q.date = data
    elif col == 'bibnum':
        data = int(data)
        q.bib_num = data
    elif col == 'dnf':
        data = data
        q.dnf = data
    elif col == 'marathon':
        q.marathon = data
    else :
        q.record = data

    db.commit()

# db의 특정 row삭제
def delete_record(db:Session, id):
    id = id
    q = db.query(Records).get(id)
    db.delete(q)
    db.commit()

# db의 모든 데이터 삭제
def delete_all(db:Session):
    db.query(Records).delete()
    db.commit()