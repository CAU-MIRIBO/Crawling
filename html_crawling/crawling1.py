from urllib import request
import requests
from bs4 import BeautifulSoup
from newspaper import Article


def crawling_article(soup):
    article=Article(url)
    article.download()

    article.parse()
    title=article.title
    contents=article.text
    if article.keywords:
        a_keywords=article.keywords
        
    if article.summary:
        a_summary=article.summary
    
    
    return title, contents

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

# 'http://m.cine21.com/news/view/?mag_id=99342'
# 'https://www.hani.co.kr/arti/society/health/1036414.html?_fr=mt1'
#  'https://www.nongmin.com/opinion/OPP/SWE/CW/349014/view?site_preference=normal'


url='https://www.nongmin.com/opinion/OPP/SWE/CW/349014/view?site_preference=normal'


    
title, content =request_through_url(url)
print_test_result(title, content)
print('process done')