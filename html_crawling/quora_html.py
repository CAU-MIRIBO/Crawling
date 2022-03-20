from tkinter import EW
from urllib import request
import requests
from bs4 import BeautifulSoup

def quora_process(url):
    ques=0
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