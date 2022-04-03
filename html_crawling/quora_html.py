from bs4 import BeautifulSoup
from selenium_crawling import *

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

# # 예시 실행 코드
# url='https://moviesnmore.quora.com/What-will-be-the-best-movie-of-2021-4'
# ques=Quora()
# a,b,c,d=ques.quora_process(url)

        