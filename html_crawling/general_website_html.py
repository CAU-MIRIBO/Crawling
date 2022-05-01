from bs4 import BeautifulSoup
from selenium_crawling import *
from newspaper import Article


# # 처음 시작할때 Webdriver 관련 오류 해결방법 -----
# from webdriver_manager.chrome import ChromeDriverManager
# driver = webdriver.Chrome(ChromeDriverManager().install())
# from gensim.summarization.summarizer import summarize
# from newspaper import Article

class Default:
    url=''
    status=0
    title=0
    paragraph=0
    content=0
    
    # general website process
    def general_website_process(self, url):
        
        status=0        
        title=0
        content_paragraph=[]
        content_all=0
        head_src=0
        
        # Case 1
        try:
            status, title, content_paragraph, content_all=self.crawl_article_newspaper_mod(url)
        except:
            print('newspaper3k not working. New approach plz')
            status=0
        
       # Case 2
        if status==200:
                return status, title, content_paragraph, content_all
        else:
            try:
                print('2nd option ==============selenium approach====================')
                status, title, content_paragraph, content_all=self.crawl_article_lastchance(url)
            except:
                print('Something wrong with selenium crawling = go to 3rd option - 1 ')
                status=0
        
        
        title, content_paragraph, content_all=self.fill_output(title, content_paragraph, content_all)
            
        return status, title, content_paragraph, content_all
    
    # Case 1 => newspaper 모듈을 사용한 크롤링
    def crawl_article_newspaper_mod(self, url):
        
        # output이 될 아이들
        a_status=0
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
            return 0, 0, 0, 0
        
        a_status=200
        a_title=article.title
        a_paragraph, a_content=self.refine_content(content)
        
        return a_status, a_title, a_paragraph, a_content
    
    # Option 2 -> selenium 모듈을 사용한 크롤링
    def crawl_article_lastchance(self, url):
        
        status=0
        title=0
        paragraph=0
        content_all=0
        
        try:
            # selenium으로 크롤링
            head, body, driver=request_with_selenium_raw(url)
        except:
            print('Error in Selenium __ crawl_article_lastchance')
            return 0, 0, 0, 0, 0
            
        try:
            title=driver.title
            content_part=driver.find_element_by_tag_name('body')
            content_text=content_part.text
            paragraph, content_all=self.refine_content(content_text)
        except:
            print('Error after Selenium on query part')
            title, paragraph, content_all=self.fill_output(title, paragraph, content_all)
            
        driver.close()
        
        # check title and content
        if not self.check_output(title, content_all):
            title, a_description=self.check_header_metadata(head)
            paragraph, content=self.refine_content(a_description)
            status=200
        else:
            print('Selenium worked well')
            status=200
            
        return status, title, paragraph, content_all
            
    
    
    # 별거 없는 함수 나중에 지우자
    def crawl_general_concept(self, url):
        cleaner=Cleaner()
        cleaner.javascript=True
        cleaner.style=True
        
        a=lxml.html.tostring(lxml.html.parse(url))
        aa=lxml.html.tostring(cleaner.clean_html(a))
    
                
            
    # Option 3 -> header meta-data summary
    def check_header_metadata(self, head):
        
        l_head=BeautifulSoup(head, 'html.parser')
        # g_type=l_head.find('meta', {'property' :'og:type'}).attrs['content']
        g_title=l_head.find('meta', {'property':'og:title'}).attrs['content']
        g_description=l_head.find('meta', {'property': 'og:description'}).atrrs['content']
        
        return g_title, g_description
        
    
    # 중복 또는 불필요한 문단 제거 - newspaper_mod에서 사용
    def refine_content(self, string):
        # 문단화
        paragraph=string.split('\n\n')
        
        # 빈 문단 제거
        paragraph=[(p) for p in paragraph if not p.isspace()]
        
        # 중복되는 문단 제거 // 사진 참조 같은 경우 중복되는 경우 다수
        f_paragraph=list(dict.fromkeys(paragraph))
        f_content=''.join(f_paragraph)
        
        return f_paragraph, f_content
    
    # Case 1 내부 함수 ==> check content --> newspaper3k 모듈이 실행하지 못하면 False
    def check_content(self, string):
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
                print(description)
                return False
            else:
                print('description enough to use')
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
            print('No contents : Just 0')
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



# url='https://www.ajunews.com/view/20211215155407703'
# url='https://www.quora.com/How-is-the-culture-of-Jeju-Island-different-from-the-rest-of-South-Korea'
# url='https://www.hani.co.kr/arti/culture/culture_general/1023318.html'
# 'https://moviesnmore.quora.com/What-will-be-the-best-movie-of-2021-4'
# url='https://owl.purdue.edu/owl/subject_specific_writing/journalism_and_journalistic_writing/writing_leads.html'
# url='https://developer.mozilla.org/en-US/docs/Web/API/Element/remove' # 이거이거 문제가 있네
# url='https://blog.naver.com/maximusc/222698515250' # selenium 으로도 안됨....
# url='https://blog.naver.com/tmddlf/222700811326' # 네이버 블로그 전체적으로 작동 어려움
# url='https://overseas.mofa.go.kr/ae-dubai-ko/brd/m_10772/view.do?seq=1342548'  #자가격리 잘 돌아간다
# url='https://kin.naver.com/qna/detail.naver?d1id=6&dirId=6010102&docId=418095586&qb=7J6Q6rCA6rKp66as&enc=utf8&section=kin.ext&rank=1&search_sort=0&spq=0'
# url='https://newsis.com/view/?id=NISX20220428_0001851291&cID=10401&pID=10400'
# url='https://newsis.com/view/?id=NISX20220428_0001851291&cID=10401&pID=10400'
# url='https://edition.cnn.com/2022/04/28/tech/elon-musk-twitter-leadership/index.html'
# url='https://www.seoul.co.kr/news/newsView.php?id=20220502001007&wlog_sub=svt_006'
# url='https://sports.news.naver.com/news?oid=109&aid=0004605358'
# url='https://blog.naver.com/tngo1005/222717248571'
# url='https://section.blog.naver.com/OfficialBlog.naver?currentPage=1'
# url='https://www.google.com/search?q=python+replace&oq=spython+replace&aqs=chrome.1.69i57j0i13l9.5410j0j4&sourceid=chrome&ie=UTF-8'
url='https://en.wikipedia.org/wiki/Game_of_Thrones'
url='https://www.rottentomatoes.com/tv/game_of_thrones'


arti=Default()
# tt, ti, hapy=arti.crawl_article_lastchance(url)
# arti.crawl_general_concept(url)
# a, b, c=arti.crawl_article_newspaper_mod(url)
# arti.crawling_article(url)
# title, contents=request_through_url(url)

status, title, para, content_all=arti.general_website_process(url)
arti.print_test_result(title, para)