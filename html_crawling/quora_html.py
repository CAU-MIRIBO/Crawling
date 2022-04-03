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
    
    body, driver=request_with_selenium(url)
    root_container=body.find_element_by_id('root')
    
    root_html=root_container.get_attribute('innerHTML')
    root_html=BeautifulSoup(root_html, 'html.parser')
    
    # q_title, q_type, q_image, q_description=get_meta_property(driver)

    # q_title=root_container.find_element_by_xpath('//*[@id="mainContent"]/div[1]/div/div[1]/span/span/div/div/div')
    # q_title=root_container.find_element_by_xpath('//body[contains(@class, question_title)]')
    q_title=root_container.find_element_by_xpath('//*[@id="mainContent"]/div[1]/div').text
    q_answer_box=root_html.find(attrs={'class':'q-box spacing_log_answer_content puppeteer_test_answer_content'})
    
    
    # q_answer_box=body.find_element_by_xpath('//*[@id="mainContent"]/div[2]/div[3]/div/div/div/div/div/div[1]')
    q_answer_list=q_answer_box.find_all('p')        # click_more(q_answer_box)
    
    
    for answ in q_answer_list:
        quo_answer_list.append(answ.text)        
        print(answ.text)
    
    # for debugging
    print_paragraph(quo_answer_list)
    
    quo_ques=q_title
    
    driver.close()
    return quo_ques, quo_ques_cont, quo_answer_list, quo_full_answer
    
def get_meta_property(src):
    
    head_container=src.find_element_by_tag_name('head')
    head_container=head_container.get_attribute('innerHTML')
    q_head=BeautifulSoup(head_container, 'html.parser')
    
    q_title=q_head.find(attrs={'property':'og:title'}).text
    q_type=q_head.find(attrs={'property':"og:type"}).text
    q_image=q_head.find(attrs={'property':'og:image'}).text
    q_description=q_head.find(attrs={'property':'og:description'}).text

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

url='https://www.quora.com/What-is-the-strangest-culture-shock-you-experienced-when-visiting-South-Korea-for-the-first-time'
# ques, answer=request_through_url(url)
# https://www.quora.com/How-is-the-culture-of-Jeju-Island-different-from-the-rest-of-South-Korea
# https://www.quora.com/What-is-the-strangest-culture-shock-you-experienced-when-visiting-South-Korea-for-the-first-time
a,b,c=quora_process(url)
