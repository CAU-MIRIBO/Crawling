from urllib import request
import requests
from bs4 import BeautifulSoup
from newspaper import Article
#import nltk

import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

# from gensim.summarization.summarizer import summarize
# from newspaper import Article

def crawling_article(soup):
    
    # nltk.download()
    article=Article(url)
    article.download()

    # print(article.html)
    article.parse()
    title=article.title
    if article.text:
        contents=article.text
    else:
        contents=''
        print('no contents')
        get_contents(soup)
    
    # print(article.text)
    # article.nlp()
    if article.keywords:
        a_keywords=article.keywords
        
    if article.summary:
        a_summary=article.summary
        
    
    return title, contents

def article_nlp(art):
    art.nlp()
    print()
    
def get_contents(soup):
    body=soup.body
    contents_text=body.text
    print(contents_text)
    
def header_process(soup):
    # g_title=g_head.find(attrs={'property':'og:title'})
    # g_container=soup.body
    # g_content=g_container #.find(attrs={'class':'e-content post-content'})
    # contents=g_content.text
    
    print('not completed')

def request_through_url(url):
    response=requests.get(url)
    if response.status_code==200:
        html=response.text
        soup=BeautifulSoup(html, 'html.parser')
        title, contents=crawling_article(soup)
        # print_test_result(title,contents)
        return title, contents
        
    else:
        print(response.status_code)
        
        
def request_with_selenium(Url):
    driver = webdriver.Chrome(executable_path='chromedriver')
    driver.get(url=Url)
    print(driver.current_url)
    driver.close()
    
    driver.implicitly_wait(time_to_wait=5)
        
def print_test_result(title, contents):
    
    print('================process done========================')
    print('\n----------Title-----------\n')
    print(title)
    print('\n-------------Content---------------\n')
    print(contents)
    print('\n')



url='https://www.ajunews.com/view/20211215155407703'
# 
# 'https://www.hani.co.kr/arti/culture/culture_general/1023318.html'
title, contents=request_through_url(url)
print_test_result(title,contents)