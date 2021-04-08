import pandas as pd
import numpy as np
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#csv파일 불러오기
df = pd.read_csv("test.csv",encoding = 'euc-kr')

#제목에 따라 오토 카라반 글램핑 칼럼 값을 변경한다.
for i in df.index.values:
    if ('오토' in df.iloc[i]['야영장명']):
        df.loc[(df.컨텐츠ID == i + 1), '오토'] = 'Y'
    if ('카라반' in df.iloc[i]['야영장명']):
        df.loc[(df.컨텐츠ID == i + 1), '카라반'] = 'Y'
    if ('글램핑' in df.iloc[i]['야영장명']):
        df.loc[(df.컨텐츠ID == i + 1), '글램핑'] = 'Y'

#태그에 필요한 칼럼만 가져온다.
test = df[['컨텐츠ID', '야영장명','입지구분','오토','글램핑','카라반','개인 트레일러 동반 여부','부대시설','체험프로그램 여부','캠핑장비대여','애완동물출입']]


# 결측치 값 없음으로 변경
test=test.fillna('없음')

#데이터라는 데이터프레임을 만들어 캠핑장 별 태그를 만들어준다.
data = pd.DataFrame(columns=['캠핑장ID','야영장명','태그'])


# 태그화 실시
for i in range(0, 2490):
    tag = ''
    if ('산' in test.iloc[i]['입지구분']):
        tag += '산맥'
        tag += ' '
    if ('계곡' in test.iloc[i]['입지구분']):
        tag += '계곡'
        tag += ' '
    if ('섬' in test.iloc[i]['입지구분']):
        tag += '섬섬'
        tag += ' '
    if ('호수' in test.iloc[i]['입지구분']):
        tag += '호수'
        tag += ' '
    if ('숲' in test.iloc[i]['입지구분']):
        tag += '수풀'
        tag += ' '
    if ('바다' in test.iloc[i]['입지구분']):
        tag += '바다'
        tag += ' '
    if ('도심' in test.iloc[i]['입지구분']):
        tag += '도심'
        tag += ' '
    if ('강' in test.iloc[i]['입지구분']):
        tag += '강가'
        tag += ' '
    if '물놀이' in test.iloc[i]['부대시설']:
        tag += '수영장'
        tag += ' '
    if (test.iloc[i]['오토'] == 'Y'):
        tag += '오토'
        tag += ' '
    if (test.iloc[i]['글램핑'] == 'Y'):
        tag += '글램핑'
        tag += ' '
    if (test.iloc[i]['카라반'] == 'Y'):
        tag += '카라반'
        tag += ' '
    if (test.iloc[i]['애완동물출입'][:2] == '가능'):
        tag += '애완견'
        tag += ' '
    if '산책로' in test.iloc[i]['부대시설']:
        tag += '산책로'
        tag += ' '
    if '놀이터' in test.iloc[i]['부대시설'] or '트렘폴린' in test.iloc[i]['부대시설']:
        tag += '아이들'
        tag += ' '
    if (test.iloc[i]['캠핑장비대여'] != '없음'):
        tag += '장비'
        tag += ' '
    if (test.iloc[i]['체험프로그램 여부'] == 'Y'):
        tag += '체험'
        tag += ' '
    if (test.iloc[i]['개인 트레일러 동반 여부'] == 'Y'):
        tag += '트레일러'
        tag += ' '

    new_data = {
        '캠핑장ID': i + 1,
        '야영장명': test.loc[test['컨텐츠ID'] == i + 1].values[0][1],
        '태그': tag
    }

    data = data.append(new_data, ignore_index=True)

# 태그별로 토큰화 진행
count_vector = CountVectorizer(ngram_range=(1,1))
c_vector_tag = count_vector.fit_transform(data['태그'])
c_vector_tag.shape

#코사인 유사도를 이용하여 유사도를 계산한 다음, argsort()를 이용하여 높은 순서대로 인덱스를 보여준다.
tag_c_sim = cosine_similarity(c_vector_tag,c_vector_tag).argsort()[:,::-1]


# 코사인 유사도를 이용하여 단어의 유사도를 통해 추천
def get_recommend_camping_list(data, camping_index, top=30):
    target_camping_index = data[data['캠핑장ID'] == camping_index].index.values
    print(target_camping_index)
    sim_index = tag_c_sim[target_camping_index, :top].reshape(-1)

    sim_index = sim_index[sim_index != target_camping_index]

    result = data.iloc[sim_index][:10]
    return result

