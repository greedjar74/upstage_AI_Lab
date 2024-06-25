# kaggle NeurIPS 2024 대회 참여
- https://www.kaggle.com/competitions/leash-BELKA/overview

## 대회 주제
- 새로운 약품을 제조했을 때 특정 단백질과 결합 여부를 예측하는 모델 생성

## 프로젝트 진행
- 앙상블 기법을 사용한다.
### 앙상블 기법
- RandomForest
- GBM
- AdaBoost
- XGBoost
- LGBM

## 모델 생성
- 각각의 앙상블 기법을 사용하여 간단한 모델을 구성
- 가장 정확도가 좋은 모델을 선택하여 고도화
    - XGBoost 채택

## 다양한 기법 시도
- 모델 하이퍼 파라미터 조정
- voting

# 결과
- leader board 점수: 0.310
### 문제점 파악
- 데이터의 크기가 너무 크다
- 모든 데이터를 학습에 사용할 수 없었다.
    - 데이터에 따라 결과가 너무 달라진다.
- 데이터의 편향이 너무 심하다.
- 하드웨어 성능의 한계