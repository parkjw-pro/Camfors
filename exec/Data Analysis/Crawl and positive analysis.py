import pandas as pd
import numpy as np
import re
from konlpy.tag import Kkma,Okt
import json
import os
from pprint import pprint
from tensorflow.keras import models
from tensorflow.keras import layers
from tensorflow.keras import optimizers
from tensorflow.keras import losses
from tensorflow.keras import metrics
import nltk
import sys
from pykospacing import spacing


import soynlp
#데이터 불러오기
df = pd.read_csv("mazimac.csv",encoding = 'euc-kr')

pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
null_data = df['입지구분'].isnull()
null_data
# 조건를 충족하는 데이터를 필터링하여 새로운 변수에 저장합니다.
nantent = df[null_data]

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup

driver = webdriver.Chrome("chromedriver")
driver.implicitly_wait(5)
driver.get("https://map.naver.com/v5/search")
list = []  # link넣기
excepted = []  # 예외 야영장 이름 넣기


#크롤링하여 블로그 리뷰 10개씩 링크받아오기
# 검색창에 검색어 입력하기
size = nantent.shape[0]
for i in range(size):
    search_box = driver.find_element_by_css_selector("div.input_box>input.input_search")
    search_box.clear()
    search_box.send_keys(nantent['야영장명'].iloc[i])
    # nantent['야영장명'].iloc[i]

    # 검색버튼 누르기
    search_box.send_keys(Keys.ENTER)

    # 검색 리스트 중 맨위 누르기
    time.sleep(2)

    try:
        driver.switch_to.frame("searchIframe")
        slist = driver.find_element_by_css_selector("#app-root > div > div._2lx2y")
        # 캠핑장 이름이 잘못되면 그냥 넣어주자 리스트
        if slist.text == "조건에 맞는 업체가 없습니다.":
            excepted.append(nantent['야영장명'].iloc[i])
            list.append([])
            driver.switch_to_default_content()
            continue

        searchlist = driver.find_elements_by_css_selector("#_pcmap_list_scroll_container > ul > li")
        flag = False

        if len(searchlist) > 1:  # 결과값이 하나이상이면
            for search in searchlist:
                try:
                    result = search.find_element_by_css_selector("div._7jQRv > div._1uXIN > a")
                    address = search.find_element_by_css_selector("div._7jQRv > div.qGsds > span > a > span._3W_ec")
                except:
                    result = search.find_element_by_css_selector("a > div.YQSTs > div > span")
                    address = search.find_element_by_css_selector("a > div._2yrPK")

                adr = nantent['주소'].iloc[i].split(' ')
                si = adr[1][: -1]
                gu = adr[2]

                if (si in address.text and gu in address.text):
                    flag = True
                    break


        else:  # 결과값이 하나
            result = searchlist[0].find_element_by_css_selector("a")
            address = searchlist[0].find_element_by_css_selector("div._2yrPK")
            adr = nantent['주소'].iloc[i].split(' ')
            si = adr[1][: -1]
            gu = adr[2]
            if (si in address.text and gu in address.text):
                flag = True

        if flag == True:
            result.click()
        else:
            driver.switch_to_default_content()
            list.append([])
            continue

    except:  # 바로 블로그 리뷰가 나온다면
        trash = 0

    #     #장소 클릭 후 블로그 리뷰 클릭
    driver.switch_to_default_content()
    driver.switch_to.frame("entryIframe")
    blogreviewbutton = driver.find_elements_by_css_selector(
        "#app-root > div > div.place_detail_wrapper > div.place_section.no_margin.GCwOh > div > div > div._3XpyR._2z4r0 > div > span._1Y6hi")

    time.sleep(2)
    blogreview = False
    for button in blogreviewbutton:
        if '블로그' in button.text:
            blogreview = True
            button.find_element_by_css_selector("a").click()
    #     if blogreview == False :
    #         driver.switch_to_default_content()
    #         list.append([])
    #         continue

    # 블로그 리뷰 하나씩 확인
    time.sleep(5)
    blogs = driver.find_elements_by_css_selector(
        "#app-root > div > div.place_detail_wrapper > div:nth-child(5) > div:nth-child(4) > div:nth-child(2) > div.place_section_content > ul > li")

    if len(blogs) == 0:
        blogs = driver.find_elements_by_css_selector(
            "#app-root > div > div.place_detail_wrapper > div:nth-child(5) > div > div:nth-child(2) > div.place_section_content > ul > li")

        if len(blogs) == 0:
            blogs = driver.find_elements_by_css_selector(
                "#app-root > div > div.place_detail_wrapper > div:nth-child(4) > div > div:nth-child(2) > div.place_section_content > ul > li")

    addblog = []
    for blog in blogs:
        link = blog.find_element_by_css_selector("a > div._32TVI > span._1Z2mH")

        if '블로그' in link.text:
            addblog.append(blog.find_element_by_css_selector("a").get_attribute("href"))
    list.append(addblog)
    driver.switch_to_default_content()

driver.close()


#받아온 링크에 다시 크롤링하여 리뷰내용 받아오기
cnt = 0
campingreview = []
for i in range(len(list)):  # 리스트 만큼
    articles = []
    if (len(list[i]) != 0):  # 리뷰가 존재하다면
        for j in list[i]:  # 하나하나 들어간다.
            driver = webdriver.Chrome("chromedriver")
            driver.implicitly_wait(5)
            driver.get(j)
            driver.switch_to.frame("mainFrame")
            try:
                review = driver.find_element_by_css_selector('#printPost1 > tbody > tr > td.bcc')
            except:
                print(j)
            articles.append(review.text)
            driver.close()
    campingreview.append(articles)


#데이터 셋 구할 수 없어 영화 리뷰 데이터로 학습하여 긍정부정 분석
#영화리뷰로 학습 데이터 만들기

def read_data(filename):
    with open(filename, 'r') as f:
        data = [line.split('\t') for line in f.read().splitlines()]
        # txt 파일의 헤더(id document label)는 제외하기
        data = data[1:]
    return data

train_data = read_data('ratings_train.txt')
test_data = read_data('ratings_test.txt')


# 영화리뷰 학습
okt = Okt()

def tokenize(doc):
    # norm은 정규화, stem은 근어로 표시하기를 나타냄
    return ['/'.join(t) for t in okt.pos(doc, norm=True, stem=True)]

if os.path.isfile('train_docs.json'):
    with open('train_docs.json') as f:
        train_docs = json.load(f)
    with open('test_docs.json') as f:
        test_docs = json.load(f)
else:
    train_docs = [(tokenize(row[1]), row[2]) for row in train_data]
    test_docs = [(tokenize(row[1]), row[2]) for row in test_data]
    # JSON 파일로 저장
    with open('train_docs.json', 'w', encoding="utf-8") as make_file:
        json.dump(train_docs, make_file, ensure_ascii=False, indent="\t")
    with open('test_docs.json', 'w', encoding="utf-8") as make_file:
        json.dump(test_docs, make_file, ensure_ascii=False, indent="\t")

# 예쁘게(?) 출력하기 위해서 pprint 라이브러리 사용
pprint(train_docs[0])


#토큰 갯수
tokens = [t for d in train_docs for t in d[0]]
print(len(tokens))


text = nltk.Text(tokens, name='NMSC')

# 전체 토큰의 개수
print(len(text.tokens))

# 중복을 제외한 토큰의 개수
print(len(set(text.tokens)))

# 출현 빈도가 높은 상위 토큰 10개
pprint(text.vocab().most_common(10))

#분석 시작
# 시간이 꽤 걸립니다! 시간을 절약하고 싶으면 most_common의 매개변수를 줄여보세요.
selected_words = [f[0] for f in text.vocab().most_common(10000)]

def term_frequency(doc):
    return [doc.count(word) for word in selected_words]

train_x = [term_frequency(d) for d, _ in train_docs]
test_x = [term_frequency(d) for d, _ in test_docs]
train_y = [c for _, c in train_docs]
test_y = [c for _, c in test_docs]


#타입 변경(64면 너무 커서 힘듬 그래서 32로 바꿈)
x_train = np.asarray(train_x).astype('float32')
x_test = np.asarray(test_x).astype('float32')

y_train = np.asarray(train_y).astype('float32')
y_test = np.asarray(test_y).astype('float32')

#모델링 시작
model = models.Sequential()
model.add(layers.Dense(64, activation='relu', input_shape=(10000,)))
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))

model.compile(optimizer=optimizers.RMSprop(lr=0.001),
             loss=losses.binary_crossentropy,
             metrics=[metrics.binary_accuracy])

model.fit(x_train, y_train, epochs=10, batch_size=512)
results = model.evaluate(x_test, y_test)

#긍정 부정 분석 후 긍정에 대해 True값 반환
def predict_pos_neg(review):
    token = tokenize(review)
    tf = term_frequency(token)
    data = np.expand_dims(np.asarray(tf).astype('float32'), axis=0)
    score = float(model.predict(data))
    if(score >= 0.5):
        return True

#예제
predict_pos_neg("가족과 오면 좋아요")
predict_pos_neg("주말은 예약하기 힘들어서")
predict_pos_neg("사이트 전기 안되고 1만원")
predict_pos_neg("원래 골프장으로 만들어서 필드가 아주 예쁨")
predict_pos_neg("노을 캠핑장은 조용히 도란도란 즐기기 좋았다")


#해쉬태그는 따로 태그화
def Hashtaganalysis(sentence):  # 형태소 분석 후 입지 나누기

    for key in locationkeys:
        for value in location[key]:
            if value in sentence:
                loca.add(key)


#해쉬태그를 제외한 문장 긍/부정 분석
locationkeys = location.keys()

def Morphemeanalysis(sentence): #형태소 분석 후 입지 나누기
    nouns = okt.nouns(sentence)
    print(nouns)
    for key in locationkeys:
       for value in location[key]:
            if value in nouns :
                if predict_pos_neg(sentence) == True:
                    loca.add(key)

#리뷰내용을 해쉬태그 및 내용을 긍정 부정분석하여 태그화 시킨다.
location = {"도심": ['도시', '도심', '건물', '아파트'],
            '산': ['산'],
            '숲': ['숲', '그늘', '삼림', '자연'],
            '섬': ['섬'],
            '계곡': ['계곡', '줄기'],
            '강': ['강'],
            '바다': ['바다', '해변', '해수욕', '밀물', '썰물'],
            '호수': ['호수', '댐', '저수지']}

r = 0
for camping in campingreview:  # 한 캠핑장에 대한 모든 블로그 리뷰
    loca = set([])

    for review in camping:  # 블로그 리뷰 하나씩 확인
        verbs = review.split('\n')
        for verb in verbs:  # 엔터로 나눈 문장
            sentences = verb.split('.')
            for sentence in sentences:  # .로 나눈 문장
                sentence = re.sub('([a-zA-Z])', '', sentence)
                sentence = re.sub('[ㄱ-ㅎㅏ-ㅣ]+', '', sentence)
                sentence = re.sub('[-=+,/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', sentence)

                if ('#' in sentence):  # hashtag라면
                    hashtag = okt.pos(sentence, join=True)
                    for has in hashtag:
                        has = has.split('/')
                        if has[1] == 'Hashtag':
                            Hashtaganalysis(has[0][1:])
                Morphemeanalysis(sentence)

    print(loca)  # 캠핑장 하나 끝나면 출력
    print(nantent.iloc[r]['야영장명'])
    locationlist = tuple(loca)
    imsi = ''
    for i in range(len(locationlist)):
        imsi += locationlist[i]
        if i == len(locationlist) - 1:
            continue
        imsi += ','
    #     campingname = nantent.iloc[r]['야영장명']
    #     try:
    #         df.loc[(df.야영장명 == campingname),['입지구분']] = [imsi]
    #     except:
    #         print(campingname)

    r += 1