from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import math


def compute_similarity(text):
    
    para, content=refine_content1(text)
    t_para=preprocess_vectorize(para)

    para_sum_list=compute_para_similarity(t_para)
    # para_sum_list.shape

    result=filter_para(para_sum_list, para)
    print(len(result[0]))
    print(result)
    
    print('=====================================================')
    print(len(para))
    for text1, i in zip(para, para_sum_list):
        print([text1])
        print(i)
    
    return result, ''.join(result)

def refine_content1(string):
        
  if string==0:
      return 0, 0
  # 문단화
  paragraph=string.split('\n\n')

  if len(paragraph)==1:
    paragraph=string.split('\n')
  
  # 빈 문단 제거
  paragraph=[(p) for p in paragraph if not p.isspace()]
  
  # 중복되는 문단 제거 // 사진 참조 같은 경우 중복되는 경우 다수
  f_paragraph=list(dict.fromkeys(paragraph))
  f_content=''.join(f_paragraph)

  
  return f_paragraph, f_content

def preprocess_vectorize(para_list):
    p_list=para_list    
    temp_list=p_list
    tfidf=TfidfVectorizer()
    tfidf_list=tfidf.fit_transform(temp_list)

    # t_title=tfidf_list[-1]
    t_para=tfidf_list[:-1]
    return t_para

def compute_para_similarity(t_para):
    para_sim_list=[]

    # 문장간 유사도 조사
    for i, p1 in enumerate(t_para):
        sum_temp_list=[]
        for p2 in t_para:
            c=cosine_similarity(p1, p2)
            sum_temp_list.append(c)
        para_sim_list.append(sum_temp_list)

    para_sim_list=np.array(para_sim_list)
    para_sim_list=np.sort(para_sim_list)[:, 2:-2]

    # print(para_sim_list.shape)
    para_sum_list=para_sim_list.sum(axis=1)

    return para_sum_list

def filter_para(para_sum_list, para):
      
  num=para_sum_list.shape[0]
  # print(num)
  para_sum_list=para_sum_list.reshape(num)

  remove_num=math.floor(para_sum_list.shape[0]*0.1)
  # print(remove_num)
  index=np.argpartition(para_sum_list, remove_num)[remove_num:]
  index=np.array(index)

  para=np.array(para)

  return para[index]