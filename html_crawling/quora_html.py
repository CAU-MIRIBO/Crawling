from bs4 import BeautifulSoup
from selenium_crawling import *

# 코드 설명
# selenium_crawling.py의 함수 (request_with_selenium) 사용하여 작동함.
# 일단 지금은 selenium_crawling.py랑 같은 폴더 안에 넣고 쓰는게 편할듯
# 클래스 Quora에서 quora_process 함수만 콜하면 작동 
# input : url - 1개
# output : quo_ques, quo_ques_cont, quo_answer_list, quo_full_answer, status 
# quo_ques 는 질문 자체, quo_ques_content는 질문 내용인데 사실 질문 내용은 quora엔 없는듯 그래서 그냥 항상 0임
# quo_answer_list는 답변 내용을 문단화 한것
# quo_full_answer는 답변 내용 전체가 한 스트링으로 다 들어있는 변수, quo_answer_list에서 나눈 문단이 겁나 짧을 때도 있어서 걍 합친 버전도 리턴하도록 함
# status : selenium에서 오류나면 output 0으로

# 여튼 오류나면 0, 0, [0], 0, 0 으로 아웃풋
# quora needs selenium
class Quora:
    def __init__(self):
        self.state=0
        
    def quora_process(self, url):

        # outputs 아마 5개가 될 예정
        quo_ques=0
        quo_ques_cont=0
        quo_answer_list=[0]
        quo_full_answer=0
        status=0

        # Selenium part
        try:
            # selenium으로 html소스 가져오기 [head, body]
            head, body=request_with_selenium(url)
        except Exception as eq:
            print("Error in quora_html.py - somehow selenium not working\n >>>> ")
            print(eq)
            return quo_ques, quo_ques_cont, quo_answer_list, quo_full_answer, status

        # body part
        try:
            body_soup=BeautifulSoup(body, 'html.parser')
        except Exception as eq:
            print("Error in quora_html.py - BeautifulSoup parser not working\n")
            print(eq)

        # get meta propterty
        try:
            q_title, q_type, q_image, q_description=self.get_meta_property(head)
            quo_ques=q_title
        except Exception as eq:
            print("Error in  quora_html.py meta property - 근데 이건 오류 나도됨 걍 패쓰~~!!\n ")
            print(eq)
        
        # q_title // q_answer
        try: 
            quo_ques=body_soup.find(attrs={'class':'q-text puppeteer_test_question_title'}).text
            q_answer_box=body_soup.find(attrs={'class':'q-box spacing_log_answer_content puppeteer_test_answer_content'})
        except Exception as eq:
            print("Error in quora_html.py - wrong in getting title or answer\n ")
            print(eq)

        # answer paragraph 별로 리스트에 저장
        try:
            q_answer_list=q_answer_box.find_all('p')
            
            for answ in q_answer_list:
                quo_answer_list.append(answ.text)

            # get whole answer in 1 variable
            quo_full_answer=q_answer_box.text
        except Exception as eq:
            print("Error in quora_html.py - answer paragraph 부분 : 걍 잘못되었을 때 넘어가라구 패쓰~\n ") 

        ## for debugging
        # self.print_test_result(q_title, quo_answer_list)
    
        quo_ques, quo_ques_cont, quo_answer_list, quo_full_answer, status=self.fill_output(quo_ques, quo_ques_cont, quo_answer_list, quo_full_answer, status)
        return quo_ques, quo_ques_cont, quo_answer_list, quo_full_answer, status

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

    def fill_output(self, quo_ques, quo_ques_cont, quo_answer_list, quo_full_answer, status):
        count=0
        if not quo_ques :
            quo_ques=0
            count+=1
        
        if not quo_full_answer:
            quo_full_answer=0
            count+=1

        if count==2:
            status=0
        else:
            status=200
        
            
        return quo_ques, quo_ques_cont, quo_answer_list, quo_full_answer, status

# # ques, answer=request_through_url(url)
# # https://www.quora.com/How-is-the-culture-of-Jeju-Island-different-from-the-rest-of-South-Korea
# # url='https://www.quora.com/Is-Hades-the-best-game-of-2020'

# # 예시 실행 코드
# url='https://moviesnmore.quora.com/What-will-be-the-best-movie-of-2021-' --url  틀린 경우 0
# ques=Quora()
# a,b,c,d,e=ques.quora_process(url)
# # ques.print_test_result(a, c)
# print(e)

        