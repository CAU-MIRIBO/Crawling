from xml.dom.minidom import Document
from bs4 import BeautifulSoup
from yaml import CBaseLoader
from selenium_crawling import *
from newspaper import Article

import urllib.request
import lxml.html
from lxml.html.clean import Cleaner
import time


# # 처음 시작할때 Webdriver 관련 오류 해결방법 -----
# from webdriver_manager.chrome import ChromeDriverManager
# driver = webdriver.Chrome(ChromeDriverManager().install())
# from gensim.summarization.summarizer import summarize
# from newspaper import Article

class Default:

    def crawl_article_lastchance(self, url):
        
        # selenium으로 크롤링
        head, body, driver=request_with_selenium_raw(url)
        # body_soup=BeautifulSoup(body, 'html.parser')
        
        title=driver.title
        content_part=driver.find_element_by_tag_name('body')
        content_text=content_part.text
    
       
        # text_containers=driver.find_elements_by_xpath('//*[text()][count(*)=0]')
        # critical_text_container=[i for i in text_containers if i.tag_name!='a']
        
        # for i in critical_text_container:
        #     print(i.get_attribute('textContent'))
            
        driver.close()
       
        # print(content_text)    
        l_title=title
        l_contents=content_text
        l_paragraph=self.refine_content(l_contents)
        
        # self.print_test_result(l_title, l_contents)
        
        return l_title, l_paragraph, l_contents
    
    def crawl_general_concept(self, url):
        cleaner=Cleaner()
        cleaner.javascript=True
        cleaner.style=True
        
        a=lxml.html.tostring(lxml.html.parse(url))
        aa=lxml.html.tostring(cleaner.clean_html(a))
    
    def general_website_process(self, url):
        
        status=0        
        title=0
        content_paragraph=[]
        content_all=0
        
        
        try:
            status, title, content_paragraph=self.crawl_article_newspaper_mod(url)
        except:
            print('newspaper3k not working. New approach plz')
            status=200
        
        if status==100:
            return title, content_paragraph, content_all
        else:
            print('2nd option ==============selenium approach====================')
            title, content_paragraph, content_all=self.crawl_article_lastchance(url)

        
        return title, content_paragraph, content_all
            
        
            
    # newspaper 모듈 사용할 수 있을까봐 임시로 만들어놓은 함수 - 1
    def check_article(self, l_head):
        g_type=l_head.find('meta', {'property' :'og:type'}).attrs['content']
        
        if g_type is 'Article':
            return True
        else:
            return False
    
    # newspaper 모듈 사용할 수 있을까봐 임시로 만들어놓은 함수 - 2
    def crawl_article_newspaper_mod(self, url):
        
        # output이 될 아이들
        a_status=100
        a_title=0
        a_content_paragraph=0
        
        article=Article(url)
        article.download()
        
        html=article.html
        article.parse()
        
        content=article.text
        image=article.top_image
        
        if self.check_content(content):
            print('do some other operation maybe with selenium')
            return 200, 0, 0
        
        a_title=article.title
        a_content_paragraph=self.refine_content(content)
        
        # nlp 작동 벗 쓰레기
        # article.nlp()
        # keywords=article.keywords
        # summary=article.summary
        # print(a_content)
        
        return a_status, a_title, a_content_paragraph
        
    
    # 중복 또는 불필요한 문단 제거 - newspaper_mod에서 사용
    def refine_content(self, string):
        # 문단화
        paragraph=string.split('\n\n')
        # self.print_each_para(paragraph)
        
        # 빈 문단 제거
        paragraph=[(p) for p in paragraph if not p.isspace()]
        # self.print_each_para(paragraph)
        
        # 중복되는 문단 제거 // 사진 참조 같은 경우 중복되는 경우 다수
        f_paragraph=list(dict.fromkeys(paragraph))
        # self.print_each_para(f_paragraph)
        
        return f_paragraph
    
    # check content - newspaper_mod 함수에서 사용 --> newspaper3k 모듈이 실행하지 못하면 False
    def check_content(self, string):
        if 'Something went wrong. Wait a moment and try again.' in string: # 모듈 아웃풋이 저 스트링임
            return True
        elif not string:
            return True
        else:
            return False
        
    def print_each_para(self, list):
        for i in list:
            print(i)
            print('\n')
        print('==========================================')
        
    def header_process(self, soup):
        # g_title=g_head.find(attrs={'property':'og:title'})
        # g_container=soup.body
        # g_content=g_container #.find(attrs={'class':'e-content post-content'})
        # contents=g_content.text
        
        print('not completed')
    
            
    def print_test_result(self, title, content_para):
        
        print('================process done========================')
        print('\n----------Title-----------\n')
        print(title)
        print('\n-------------Content---------------\n')
        self.print_each_para(content_para)
        print('\n')



url='https://www.ajunews.com/view/20211215155407703'
# url='https://www.quora.com/How-is-the-culture-of-Jeju-Island-different-from-the-rest-of-South-Korea'
# url='https://www.hani.co.kr/arti/culture/culture_general/1023318.html'
# 'https://www.ajunews.com/view/20211215155407703'
# 'https://moviesnmore.quora.com/What-will-be-the-best-movie-of-2021-4'
url='https://owl.purdue.edu/owl/subject_specific_writing/journalism_and_journalistic_writing/writing_leads.html'
url='https://developer.mozilla.org/en-US/docs/Web/API/Element/remove' # 이거이거 문제가 있네
url='https://blog.naver.com/maximusc/222698515250' # selenium 으로도 안됨....
url='https://blog.naver.com/tmddlf/222700811326' # 네이버 블로그 전체적으로 작동 어려움
url='https://overseas.mofa.go.kr/ae-dubai-ko/brd/m_10772/view.do?seq=1342548'
url='https://kin.naver.com/qna/detail.naver?d1id=6&dirId=6010102&docId=418095586&qb=7J6Q6rCA6rKp66as&enc=utf8&section=kin.ext&rank=1&search_sort=0&spq=0'
url='https://newsis.com/view/?id=NISX20220428_0001851291&cID=10401&pID=10400'

arti=Default()
# tt, ti, hapy=arti.crawl_article_lastchance(url)
# arti.crawl_general_concept(url)
# a, b, c=arti.crawl_article_newspaper_mod(url)
# arti.crawling_article(url)
# title, contents=request_through_url(url)

a, b, c=arti.general_website_process(url)
arti.print_test_result(a,b)