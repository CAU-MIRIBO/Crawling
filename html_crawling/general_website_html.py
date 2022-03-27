from re import A
from tkinter import EW
from urllib import request
import requests
from bs4 import BeautifulSoup
from newspaper import Article

# from gensim.summarization.summarizer import summarize
# from newspaper import Article

def crawling_article(soup):
    article=Article(url)
    article.download()

    print(article.html)
    article.parse()
    title=article.title
    contents=article.text
    
    # print(article.text)
    if article.keywords:
        a_keywords=article.keywords
        
    if article.summary:
        a_summary=article.summary
        
    
    return title, contents

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
        
        
def print_test_result(title, contents):
    
    print('================process done========================')
    print('\n----------Question Header-----------\n')
    print(title)
    print('\n-------------Answer---------------\n')
    print(contents)
    print('\n')



url='https://www.hani.co.kr/arti/culture/culture_general/1023318.html'
# 'https://www.ajunews.com/view/20211215155407703'
    
request_through_url(url)
print('process done')
