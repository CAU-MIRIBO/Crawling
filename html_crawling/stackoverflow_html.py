from tkinter import EW
from urllib import request
import requests
from bs4 import BeautifulSoup


def stackOverflow_process(soup):
    # print(soup)
    
    # get question header
    ques_header=soup.find(attrs={'id': 'question-header'})
    ques_header=ques_header.find('h1')
    ques=ques_header.text
    
    # get question contents
    ques_content1=soup.find(attrs={'class':'question'})
    ques_content2=ques_content1.find(attrs={'class':'s-prose js-post-body'})
    ques_content=ques_content2.text
    
    #질문 부분의 댓글에 대해서도 생각해보기
    
    
    #get selected answer
    ans_container=soup.find(attrs={'id': 'answers'})
    
    # if there is no answer at all
    
    #if there is selected answer
    if ans_container.find(attrs={'class': 'answer js-answer accepted-answer'}):
        selected_ans_container=ans_container.find(attrs={'class': 'answer js-answer accepted-answer'})
        
    else:
        #if there is no selected answer
        print('-----------currently no selected answer---------------')
        all_answers=ans_container.find_all(attrs={'class':'answer js-answer'})
        
        # select answer with max data-score
        score_list=[]
        for (i, lst) in enumerate(all_answers):
            score_list.append(int(lst.attrs['data-score']))
        
        selected_ans_index=score_list.index(max(score_list))
        selected_ans_container=all_answers[selected_ans_index]
        
        print('a')
    
    # 답변의 댓글에 대해서도 생각해봐야한다
        
    selected_ans_content=selected_ans_container.find(attrs={'class' : 's-prose js-post-body'})
    answer_text=selected_ans_content.text

    return ques, ques_content, answer_text

# For Debugging        
def print_test_result(question, ques_detail, answer):
    
    print('================process done========================')
    print('-----Question-----------')
    print(question)
    print(ques_detail)
    print('-------------answer---------------')
    print(answer)
    
    
def request_through_url(url):
    response=requests.get(url)
    if response.status_code==200:
        html=response.text
        soup=BeautifulSoup(html, 'html.parser')
        question, ques_detail, answer=stackOverflow_process(soup)
        print_test_result(question, ques_detail, answer)
        
    else:
        print(response.status_code)
        

url='https://stackoverflow.com/questions/82831/how-do-i-check-whether-a-file-exists-without-exceptions?rq=1'
request_through_url(url)
    