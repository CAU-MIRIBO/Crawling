from bs4 import BeautifulSoup
from html_crawling.selenium_crawling import *
from newspaper import Article
from similarity import *

# 5/14 ver

# 코드 설명
# selenium_crawling.py의 함수 (request_with_selenium) 사용하여 작동함.
# 일단 지금은 selenium_crawling.py랑 같은 폴더 안에 넣고 쓰는게 편할듯
# 클래스 Default에서 general_website_process 함수만 콜하면 작동 
# input : url - 1개
# output : status, title, content_paragraph, content_all
# status : 오류나거나 크롤링 내용 별거 없을 때 0 반환
# ritle 는 글제목, content_paragraph는 문단화 한 내용, content_all은 문단화 하지 않은 전체 글

# 여튼 오류나면 0, 0, [0], 0, 0 으로 아웃풋
# quora needs selenium

# ================== 실행방법은 요러케 =====================
# arti=Default()
# status, title, para, content_all=arti.general_website_process(url)
# arti.print_test_result(title, para)



class Default:
    # url=''
    d_status=0
    d_title=0
    d_paragraph=0
    d_content=0
    
    # general website process
    def general_website_process(self, url):
        
        status=0        
        title=0
        content_paragraph=[]
        content_all=0
        
        # Case 1
        try:
            print('Case 1 - Trying')
            status, title, content_all=self.crawl_article_newspaper_mod(url)
        except:
            status=0
            
        if status==200:
            content_paragraph, content_all=self.refine_content(content_all)
            if self.check_output(title, content_all):
                self.d_status=200
                self.d_title=title
                self.d_paragraph=content_paragraph
                self.d_content=content_all
                return status, title, content_paragraph, content_all
            else:
                print('Case 1 - Fail (No content) ')
        else:
            print('Case 1 - Fail (Module not working)')
                
       # Case 2
        try:
            print('2nd option ==============selenium approach====================')
            print('Case 2 - Trying')
            status, title, content_paragraph, content_all=self.crawl_article_lastchance(url)
        except:
            print('Case 2 - Fail (exception in lastchance)')
            status=0
        
        title, content_paragraph, content_all=self.fill_output(title, content_paragraph, content_all)
        if content_all!=0:
            content_paragraph, content_all=compute_similarity(content_all)
            
        return status, title, content_paragraph, content_all
    
    # Case 1 => newspaper 모듈을 사용한 크롤링
    def crawl_article_newspaper_mod(self, url):
        
        # output이 될 아이들
        a_status=0
        a_title=0
        a_content=0
        
        article=Article(url)
        article.download()
        
        html=article.html
        article.parse()
        
        a_status=200
        a_title=article.title
        a_content=article.text
        # image=article.top_image
        
        # check if content is 'Something went wrong. Wait a moment and try again.'
        if self.check_content_from_news(a_content):
            print('=> in Case 1 - Fail (No contents - module not supported) ')
            return 0, 0, 0
        
        # a_paragraph, a_content=self.refine_content(content)
        
        return a_status, a_title, a_content
    
    # Option 2 -> selenium 모듈을 사용한 크롤링
    def crawl_article_lastchance(self, url):
        
        status=0
        title=0
        paragraph=0
        content_all=0
        
        # try:
            # selenium으로 크롤링
        head, body, driver=request_with_selenium_raw(url)
        # except:
        #     print('=> in Case 2 - Fail (Selenium module not working)')
        #     return 0, 0, 0, 0
            
        try:
            title=driver.title
            content_part=driver.find_element_by_tag_name('body')
            content_text=content_part.text
            paragraph, content_all=self.refine_content(content_text)
        except:
            print('=> in Case 2 - Fail (Exception in querying HTML/js)')
            title, paragraph, content_all=self.fill_output(title, paragraph, content_all)
            
        driver.close()
        
        # check title and content
        if not self.check_output(title, content_all):
            title, a_description=self.check_header_metadata(head)
            paragraph, content=self.refine_content(a_description)
            status=200
        else:
            status=200
            
        
            
        return status, title, paragraph, content_all
            
    # Option 3 -> header meta-data summary
    def check_header_metadata(self, head):
        
        l_head=BeautifulSoup(head, 'html.parser')
        # g_type=l_head.find('meta', {'property' :'og:type'}).attrs['content']
        g_title=l_head.find('meta', {'property':'og:title'}).attrs['content']
        g_description=l_head.find('meta', {'property': 'og:description'}).atrrs['content']
        
        return g_title, g_description
        
    
    # 중복 또는 불필요한 문단 제거 - newspaper_mod에서 사용
    def refine_content(self, string):
        
        if string==0:
            return 0, 0
        # 문단화
        paragraph=string.split('\n\n')
        
        # 빈 문단 제거
        paragraph=[(p) for p in paragraph if not p.isspace()]
        
        # 중복되는 문단 제거 // 사진 참조 같은 경우 중복되는 경우 다수
        f_paragraph=list(dict.fromkeys(paragraph))
        f_content=''.join(f_paragraph)
        
        return f_paragraph, f_content
    
    # Case 1 내부 함수 ==> check content --> newspaper3k 모듈이 실행하지 못하면 False
    def check_content_from_news(self, string):
        if 'Something went wrong. Wait a moment and try again.' in string: # 모듈 아웃풋이 저 스트링임
            return True
        elif not string:
            return True
        else:
            return False
        
    # Case 2 내부 함수 ==> check output data
    def check_output(self, title, description):
        if not title:
            return False
        
        if description:
            description.replace('\n', '')
            if len(description)<100:
                # ?print(description)
                return False
            else:
                # print('description enough to use')
                return True
        else:
            return False
    
    # 내부에 아무것도 없으면 0으로 채워주는 함수
    def fill_output(self, title, para, content_all):
        if not title:
            title=0
        
        if content_all:
            predict_code=content_all.count('{')+content_all.count('}')
            if predict_code>30:
                content_all=0
                para=0
        else:
            content_all=0
            para=0
            
        return title, para, content_all
    
    def print_each_para(self, list):
        if list==0:
            print(list)
            return
        for i in list:
            print(i)
            print('\n')
        print('==========================================')
            
            
    def print_test_result(self, title, content_para):
        
        print('================process done========================')
        print('\n----------Title-----------\n')
        print(title)
        print('\n-------------Content---------------\n')
        self.print_each_para(content_para)
        print('\n')