from subprocess import list2cmdline
from bs4 import BeautifulSoup
from selenium_crawling import *
from newspaper import Article

# # 처음 시작할때 Webdriver 관련 오류 해결방법
# from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(ChromeDriverManager().install())

# from gensim.summarization.summarizer import summarize
# from newspaper import Article

class Default:

    def crawling_article(self, soup):
        
        # selenium으로 크롤링
        head, body=request_with_selenium(url)
        
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
            self.get_contents(soup)
        
        # print(article.text)
        # article.nlp()
        if article.keywords:
            a_keywords=article.keywords
            
        if article.summary:
            a_summary=article.summary
            
        
        return title, contents
    
    def crawl_article_newspaper_mod(self, url):
        
        article=Article(url)
        article.download()
        
        html=article.html
        article.parse()
        
        content=article.text
        image=article.top_image
        print(content)
        
        a_title=article.title
        a_content_paragraph=self.refine_content(content)
        a_content=content
        
        # nlp 작동 벗 쓰레기
        # article.nlp()
        # keywords=article.keywords
        # summary=article.summary
        return a_title, a_content_paragraph, a_content
        
    def refine_content(self, string):
        # 문단화
        paragraph=string.split('\n\n')
        #self.print_each_para(paragraph)
        
        # 빈 문단 제거
        paragraph=[(p) for p in paragraph if not p.isspace()]
        # self.print_each_para(paragraph)
        
        # 중복되는 문단 제거 // 사진 참조 같은 경우 중복되는 경우 다수
        f_paragraph=list(dict.fromkeys(paragraph))
        self.print_each_para(f_paragraph)
        
        return f_paragraph
    
    def print_each_para(self, list):
        for i in list:
            print(i)
            print('\n')
        print('==========================================')

    def article_nlp(self, art):
        art.nlp()
        print()
    
    def get_contents(self, soup):
        body=soup.body
        contents_text=body.text
        print(contents_text)
        
    def header_process(self, soup):
        # g_title=g_head.find(attrs={'property':'og:title'})
        # g_container=soup.body
        # g_content=g_container #.find(attrs={'class':'e-content post-content'})
        # contents=g_content.text
        
        print('not completed')
    
            
    def print_test_result(self, title, contents):
        
        print('================process done========================')
        print('\n----------Title-----------\n')
        print(title)
        print('\n-------------Content---------------\n')
        print(contents)
        print('\n')



url='https://www.hani.co.kr/arti/culture/culture_general/1023318.html'
# 'https://www.quora.com/How-is-the-culture-of-Jeju-Island-different-from-the-rest-of-South-Korea'
# 'https://www.hani.co.kr/arti/culture/culture_general/1023318.html'
# 'https://www.ajunews.com/view/20211215155407703'

arti=Default()
a, b, c=arti.crawl_article_newspaper_mod(url)
# arti.crawling_article(url)
# title, contents=request_through_url(url)
# print_test_result(title,contents)