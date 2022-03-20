from re import A
from tkinter import EW
from urllib import request
import requests
from bs4 import BeautifulSoup

def general_process(soup):
    return A

def request_through_url(url):
    response=requests.get(url)
    if response.status_code==200:
        html=response.text
        soup=BeautifulSoup(html, 'html.parser')
        title, contents=general_process(soup)
        print_test_result(title,contents)
        return title, contents
        
    else:
        print(response.status_code)
        
        
def print_test_result(title, contents):
    
    print('================process done========================')
    print('\n----------Question Header-----------\n')
    print(title)
    print('\n-------------Answer---------------\n')
    print(contents)
    print('\n')
