# from tkinter import EW
from urllib import request
import requests
from bs4 import BeautifulSoup
from selenium_crawling import *

# quora needs selenium

def quora_process(url):
    
    quo_ques=0
    quo_ques_cont=0
    quo_answer=[]
    
    # q_head=soup.head
    # q_title=q_head.find(attrs={'property':'og:title'})
    # q_type=q_head.find(attrs={'property':"og:type"})
    # q_image=q_head.find(attrs={'property':'og:image'})
    # q_description=q_head.find(attrs={'property':'og:description'})
    
    # q_body=soup.body
    # q_content=q_body.find(attrs={'class':'q-box spacing_log_answer_content puppeteer_test_answer_content'})
    # q_text=q_body.text
    
    # print(q_body)
    # p_text=q_body.find_all('p')
    # ques=q_title
    # answer=0
    body, driver=request_with_selenium(url)
    root_container=body.find_element_by_id('root')

    # q_title=root_container.find_element_by_xpath('//*[@id="mainContent"]/div[1]/div/div[1]/span/span/div/div/div')
    # q_title=root_container.find_element_by_xpath('//body[contains(@class, question_title)]')
    q_title=root_container.find_element_by_xpath('//*[@id="mainContent"]/div[1]/div')
    q_answer_box=body.find_element_by_xpath('//*[@id="mainContent"]/div[2]/div[3]/div/div/div/div/div/div[1]')
    q_answer_list=q_answer_box.find_elements_by_tag_name('p')
    
    for answ in q_answer_list:
        quo_answer.append(answ.text)
        print(answ.get_attribute('innerHTML'))
        
        print(answ.text)
    
    # for debugging
    print_paragraph(quo_answer)
    # html=q_answer.get_attribute('innerHTML')
    
    # //*[@id="mainContent"]/div[2]/div[3]/div/div/div/div/div/div[1]
    # //*[@id="mainContent"]/div[2]/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div[2]/div/div[1]
    # //*[@id="mainContent"]/div[2]/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div[2]/div
    # //*[@id="mainContent"]/div[2]/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div[2]/div
    # # HTML 표시
    # //*[@id="mainContent"]/div[2]/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div[2]/div/div/div/span/p[1]
    # //*[@id="mainContent"]/div[2]/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div[2]/div/div/div/span/p[2]
   # //*[@id="mainContent"]/div[2]/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/div[2]/div/div/div/span/p[1]
   
    # )print('====================')
    # print(q_title.get_attribute('innerHTML'))
    # print('====================')
    
    quo_ques=q_title.text
    
    driver.close()
    return quo_ques, quo_ques_cont, quo_answer

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
    
def print_paragraph(answ):
    for a in answ:
        print(a)

url='https://www.quora.com/How-is-the-culture-of-Jeju-Island-different-from-the-rest-of-South-Korea'
# ques, answer=request_through_url(url)
a,b,c=quora_process(url)
