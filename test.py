import pandas as pd
import numpy as np
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

data = pd.read_csv("data.csv",encoding = 'euc-kr')

count_vector = CountVectorizer(ngram_range=(1,1))
c_vector_tag = count_vector.fit_transform(data['태그'])

tag_c_sim = cosine_similarity(c_vector_tag,c_vector_tag).argsort()[:,::-1]

# 코사인 유사도를 이용하여 단어의 유사도를 통해 추천
def get_recommend_camping_list(data,camping_title,top=30):
    target_camping_index = data[data['야영장명'] == camping_title].index.values
    
    sim_index = tag_c_sim[target_camping_index, :top].reshape(-1)
    
    sim_index = sim_index[sim_index != target_camping_index]
    result = data.iloc[sim_index][:10]
    return result

result = get_recommend_camping_list(data,camping_title = '(주)양촌여울체험캠프')
for i in result['캠핑장ID']:
    print(i)