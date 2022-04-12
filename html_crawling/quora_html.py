from bs4 import BeautifulSoup
from selenium_crawling import *

# 코드 설명
# selenium_crawling.py의 함수 (request_with_selenium) 사용하여 작동함.
# 일단 지금은 selenium_crawling.py랑 같은 폴더 안에 넣고 쓰는게 편할듯
# 클래스 Quora에서 quora_process 함수만 콜하면 작동 
# input : url - 1개
# output : quo_ques, quo_ques_cont, quo_answer_list, quo_full_answer - 현재는 4개 (나중에 웹페이지 상태 이런것도 추가될 듯)
# quo_ques 는 질문 자체, quo_ques_content는 질문 내용인데 사실 질문 내용은 quora엔 없는듯 그래서 그냥 항상 0임
# quo_answer_list는 답변 내용을 문단화 한것
# quo_full_answer는 답변 내용 전체가 한 스트링으로 다 들어있는 변수, quo_answer_list에서 나눈 문단이 겁나 짧을 때도 있어서 걍 합친 버전도 리턴하도록 함

# quora needs selenium
class Quora:
    def __init__(self):
        self.state=0
        
    def quora_process(self, url):

        # outputs 아마 5개가 될 예정
        quo_ques=0
        quo_ques_cont=0
        quo_answer_list=[]
        quo_full_answer=0
        page_state=0

        
        # selenium으로 html소스 가져오기 [head, body]
        head, body=request_with_selenium(url)

        # body part
        body_soup=BeautifulSoup(body, 'html.parser')

        # get meta propterty
        q_title, q_type, q_image, q_description=self.get_meta_property(head)

        # q_title // q_answer
        q_title=body_soup.find(attrs={'class':'q-text puppeteer_test_question_title'}).text
        q_answer_box=body_soup.find(attrs={'class':'q-box spacing_log_answer_content puppeteer_test_answer_content'})


        # answer paragraph 별로 리스트에 저장
        q_answer_list=q_answer_box.find_all('p')
        
        for answ in q_answer_list:
            quo_answer_list.append(answ.text)        
            print(answ.text)

        # get whole answer in 1 variable
        quo_full_answer=q_answer_box.text    


        # for debugging
        self.print_test_result(q_title, quo_answer_list)
        
        quo_ques=q_title
        return quo_ques, quo_ques_cont, quo_answer_list, quo_full_answer

    # meta data 보조 정보로 크롤    
    def get_meta_property(self, head):

        q_head=BeautifulSoup(head, 'html.parser')

        q_title=q_head.find('meta', {'property' :'og:title'}).attrs['content']
        q_type=q_head.find('meta', {'property' :'og:type'}).attrs['content']
        q_image=q_head.find('meta', {'property':'og:image'}).attrs['content']
        q_description=q_head.find('meta', {'property':'og:description'}).attrs['content']

        return q_title, q_type, q_image, q_description

    def print_test_result(self, question, answer):

        print('================process done========================')
        print('\n----------Question Header-----------\n')
        print(question)
        print('\n-------------Answer---------------\n')
        self.print_paragraph(answer)
        print('\n')

    def print_paragraph(self,answ):
        for a in answ:
            print(a)


# ques, answer=request_through_url(url)
# https://www.quora.com/How-is-the-culture-of-Jeju-Island-different-from-the-rest-of-South-Korea
# https://www.quora.com/What-is-the-strangest-culture-shock-you-experienced-when-visiting-South-Korea-for-the-first-time
# https://www.quora.com/What-did-you-experience-in-South-Korea-that-would-never-happen-in-Japan
# https://www.quora.com/Is-Hades-the-best-game-of-2020

# 예시 실행 코드
# url='https://moviesnmore.quora.com/What-will-be-the-best-movie-of-2021-4'
# ques=Quora()
# a,b,c,d=ques.quora_process(url)

        