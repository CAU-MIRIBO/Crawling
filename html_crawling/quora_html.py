from tkinter import EW
from urllib import request
import requests
from bs4 import BeautifulSoup

def quora_process(soup):
    
    q_head=soup.head
    q_title=q_head.find(attrs={'property':'og:title'})
    q_type=q_head.find(attrs={'property':"og:type"})
    q_image=q_head.find(attrs={'property':'og:image'})
    q_description=q_head.find(attrs={'property':'og:description'})
    
    q_body=soup.body
    q_content=q_body.find(attrs={'class':'q-box spacing_log_answer_content puppeteer_test_answer_content'})
    q_text=q_body.text
    
    print(q_body)
    p_text=q_body.find_all('p')
    ques=q_title
    answer=0
    
    return ques, answer

def request_through_url(url):
    response=requests.get(url)
    if response.status_code==200:
        html=response.text
        soup=BeautifulSoup(html, 'html.parser')
        ques, answer=quora_process(soup)
        print_test_result(ques, answer)
        return ques, answer
        
    else:
        print(response.status_code)
        
        
def print_test_result(question, answer):
    
    print('================process done========================')
    print('\n----------Question Header-----------\n')
    print(question)
    print('\n-------------Answer---------------\n')
    print(answer)
    print('\n')

url='https://www.quora.com/How-is-the-culture-of-Jeju-Island-different-from-the-rest-of-South-Korea'
ques, answer=request_through_url(url)
