# 네이버에서 주식 데이터 크롤링

import time
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By

# 네이버 증권 웹 페이지 생성
driver = webdriver.Chrome()
url = 'https://finance.naver.com/'
driver.get(url)

# 주식을 알고싶은 검색어 입력
key = input('검색어를 입력하세요: ')
# 검색창에 검색어 입력
driver.find_element(By.CLASS_NAME, 'search_input').click()
driver.find_element(By.CLASS_NAME, 'search_input').send_keys(key+'\n')
time.sleep(2)

# 검색 결과가 모여있는 구역 추출 -> 검색한 키워드 관련 회사가 나열되어 있다.
container = driver.find_element(By.CLASS_NAME, 'tbl_search').find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')

# 검색된 종목들을 보여준다.
for idx, elem in enumerate(container):
    company = elem.find_element(By.CLASS_NAME, 'tit').text
    print(f'{idx+1}. {company}')

# 종목 선택, 이동
# 사용자가 회사 하나를 선택한다.
slected_company = int(input("종목을 선택하세요(번호): "))
key = container[slected_company-1].find_element(By.CLASS_NAME, 'tit').text # 종목 저장 -> 추후 데이터 파일 생성시 파일 이름에 사용됨
print(key)
container[slected_company-1].find_element(By.CLASS_NAME, 'tit').find_element(By.TAG_NAME, 'a').click()

# 시세 클릭
driver.find_element(By.CLASS_NAME, 'tab_total_submenu').find_element(By.CLASS_NAME, 'tab2').click()
time.sleep(5)

# 주식 정보를 알기위해서 크롤링시 단순히 데이터를 불러올 수 없다. -> iframe이라는 형태
# iframe으로 이동 -> 해당 url으로 이동해야 데이터를 가져올 수 있음
container = driver.find_element(By.CLASS_NAME, 'inner_sub')
# 모든 iframe을 찾는다. -> 네이버 주식에서는 '시간별시세', '일별시세' 두 개가 존재
iframe_li = container.find_elements(By.TAG_NAME, 'iframe')
iframe_url = iframe_li[1].get_attribute('src') # 두 번째 iframe에서 '일별시세'링크를 가져온다.
driver.get(iframe_url) # '일별시세'페이지로 이동
current_url = driver.current_url # 현재 url

# 가장 마지막 페이지를 알아낸다.
driver.find_element(By.CLASS_NAME, 'pgRR').click()
last_page = driver.find_element(By.CLASS_NAME, 'Nnavi').find_element(By.CLASS_NAME, 'on').text

df = [] # 결과 파일
for page in range(1, int(last_page)): # int(last_page)으로 하면 마지막 페이지는 크롤링 불가 -> but 마지막 페이지의 경우 데이터가 없는 칸이 존재할 수 있다. 이를 처리하는 것이 힘들어 마지막 페이지는 사용하지 않는거..
    url = current_url + f'&page={page}' # 페이지를 바꿔가면서 크롤링 진행
    driver.get(url) # 페이지 이동
    container = driver.find_element(By.CLASS_NAME, 'type2').find_elements(By.TAG_NAME, 'tr') # 주가 정보 컨테이너
    print(page) # 현재 페이지 출력 

    # container에서 하나씩 뽑아온다.
    for idx, elem in enumerate(container):
        if 2<=idx<=6 or 10<=idx<=14: # 중간에 정보가 없는 것은 건너뜀
            tmp = elem.find_elements(By.TAG_NAME, 'td') # 각 요소를 분리해서 가져온다.
            tmp_li = [] # 임시로 데이터 저장 공간
            for td_idx, td in enumerate(tmp):
                if td_idx == 0: # 날짜는 저장 형태가 다르므로 따로 빼준다.
                    tmp_li.append(td.text)

                elif td_idx != 2: # 전일비는 +,- 요소 처리가 필요하므로 따로 빼준다.
                    content = td.text # 가격 정보를 가져온다.
                    tmp_li.append(int(content.replace(',', ''))) # str형태에서 int형태로 변환

                # 전일비 -> 가장 까다로움
                # tag:img or class:blind 랜덤하게 나온다..
                # 값이 0인 경우에 대해 다르게 처리 필요
                else :
                    price = td.find_element(By.CLASS_NAME, 'tah').text # 가격을 먼저 뽑아온다.
                    if price != '0': # 0이 아닌 경우 +,- 처리가 필요
                        try :
                            up_down = td.find_element(By.TAG_NAME, 'img').get_attribute('alt') # img 태그에 상승, 하락이 존재하는 경우
                        except :
                            up_down = td.find_element(By.CLASS_NAME, 'blind').text # blind클래스에 text로 상승, 하락이 존재하는 경우
                        
                        price = int(price.replace(',', '')) # 가격 정보를 str형태에서 int형태로 바꿔준다.
                        if up_down == '하락': # 하락인 경우 -를 곱해준다.
                            price *= -1

                        tmp_li.append(price) # 전일비 저장
                    else :
                        tmp_li.append(0)
            # dict형태로 데이터 생성
            df_tmp = {
                '날짜':tmp_li[0],
                '종가':tmp_li[1],
                '전일비':tmp_li[2],
                '시가':tmp_li[3],
                '고가':tmp_li[4],
                '저가':tmp_li[5],
                '거래량':tmp_li[6]
            }
            df.append(df_tmp) # 결과 변수에 추가
    time.sleep(0.3)

df = pd.DataFrame(df) # 리스트에서 dataframe형태로 변환
print(df)
df.to_csv(f'{key}_stock.csv', encoding='utf-8-sig')