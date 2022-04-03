# from tkinter import EW
from urllib import request
import requests
from bs4 import BeautifulSoup
from selenium_crawling import *

# quora needs selenium

def quora_process(url):
    
    # outputs
    quo_ques=0
    quo_ques_cont=0
    quo_answer_list=[]
    quo_full_answer=0
    page_state=0
    
    # selenium으로 html소스 가져오기 [head, body]
    head, body=request_with_selenium(url)
    # root_container=body.find_element_by_id('root')
    
    # root_html=root_container.get_attribute('innerHTML')
    body_soup=BeautifulSoup(body, 'html.parser')
    
    q_title, q_type, q_image, q_description=get_meta_property(head)
    # q_title=root_container.find_element_by_xpath('//*[@id="mainContent"]/div[1]/div/div[1]/span/span/div/div/div')
    # q_title=root_container.find_element_by_xpath('//body[contains(@class, question_title)]')
    
    q_title=body_soup.find(attrs={'class':'q-text puppeteer_test_question_title'}).text
    q_answer_box=body_soup.find(attrs={'class':'q-box spacing_log_answer_content puppeteer_test_answer_content'})
    
    
    # q_answer_box=body.find_element_by_xpath('//*[@id="mainContent"]/div[2]/div[3]/div/div/div/div/div/div[1]')
    
    # answer paragraph 별로 리스트에 저장
    q_answer_list=q_answer_box.find_all('p')        # click_more(q_answer_box)
    for answ in q_answer_list:
        quo_answer_list.append(answ.text)        
        print(answ.text)
    
    # get whole answer in 1 variable
    quo_full_answer=q_answer_box.text    
    
    
    # for debugging
    print_paragraph(quo_answer_list)
    
    quo_ques=q_title
    
    # driver.close()
    return quo_ques, quo_ques_cont, quo_answer_list, quo_full_answer
    
def get_meta_property(head):
    
    q_head=BeautifulSoup(head, 'html.parser')
    
    q_title=q_head.find('meta', {'property' :'og:title'}).attrs['content']
    q_type=q_head.find('meta', {'property' :'og:type'}).attrs['content']
    q_image=q_head.find('meta', {'property':'og:image'}).attrs['content']
    q_description=q_head.find('meta', {'property':'og:description'}).attrs['content']

    ques=q_title
    return q_title, q_type, q_image, q_description
    

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

url='https://www.quora.com/What-did-you-experience-in-South-Korea-that-would-never-happen-in-Japan'
# ques, answer=request_through_url(url)
# https://www.quora.com/How-is-the-culture-of-Jeju-Island-different-from-the-rest-of-South-Korea
# https://www.quora.com/What-is-the-strangest-culture-shock-you-experienced-when-visiting-South-Korea-for-the-first-time
a,b,c,d=quora_process(url)

        