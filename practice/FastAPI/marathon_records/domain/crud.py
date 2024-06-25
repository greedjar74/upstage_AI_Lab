# 실제로 데이터를 주고 받는 모듈

from models import Records
from sqlalchemy.orm import Session

# 전체 기록 리스트 반환
def get_records_list(db: Session):
    records_list = db.query(Records).order_by(Records.id.desc()).all()
    return records_list

# 하나의 기록 반환
def get_record_detail(db:Session, id):
    record_detail = db.query(Records).get(id)
    return record_detail

# 새로운 기록 업로드
def update_record(db: Session, title, date, bibnum, record, finish):
    record = Records(title=title, date=date, bibnum=bibnum, record=record, finish=finish)
    db.add(record)
    db.commit()

# 기록 수정
def modify_record(db:Session, id, col, data):
    q = db.query(Records).get(id)
    # 수정하려는 데이터 col에 접근하여 데이터 수정
    if col == 'date':
        q.date = data
    elif col == 'bibnum':
        data = int(data)
        q.bib_num = data
    elif col == 'finish':
        q.finish = data
    elif col == 'title':
        q.title = data
    else :
        q.record = data

    db.commit()

# 특정 기록 삭제
def delete_record(db:Session, id):
    q = db.query(Records).get(id)
    db.delete(q)
    db.commit()

# 모든 기록 삭제
def delete_all_records(db:Session):
    db.query(Records).delete()
    db.commit()