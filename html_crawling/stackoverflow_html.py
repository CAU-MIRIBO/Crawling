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
    
    #get selected answer
    ans_container=soup.find(attrs={'id': 'answers'})
    
    # if there is no answer at all
    
    #if there is selected answer
    if ans_container.find(attrs={'class': 'answer js-answer accepted-answer'}):
        selected_ans_container=ans_container.find(attrs={'class': 'answer js-answer accepted-answer'})
    else:
        #if there is no selected answer
        print('-----------currently no selected answer---------------')
        
        
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
        

url='https://stackoverflow.com/questions/33238091/test-if-children-tag-exists-in-beautifulsoup'
request_through_url(url)
    