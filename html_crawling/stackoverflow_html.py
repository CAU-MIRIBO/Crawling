import json

import requests
from bs4 import BeautifulSoup

import re

# stackoverflow_html.py 코드 설명
# class Stackoverflow에서 stackOverflow_process 콜하여 사용 가능
# stackOverflow_process 함수 output 5개 - default 아웃풋은 0, 0, 0, 0, 0
# (뭐가 안되거나 request 잘못 작동하면 output=0 )

# ques_header = 질문 제목, ques_content = 질문 내용
# selected_ans_content = 채택 답변(답변이 아예 없을 경우 10000)
# keyword_list = 키워드들 리스트 형태 리턴, status = 웸페이지 로딩 상태 - 정상적이라면 200

# status 에 관련해서는 앞으로 논의 필요 - 몇번 다시 시도할지 등
# 클래스 사용 예시는 맨 아래
# 예외처리 일단 하기는 했는데 사실 별거 없음 걍 에러 로깅만 가능하게 해놓음

class Stackoverflow:

    def __init__(self):
        self.state=0


    def stackOverflow_process(self, url):

        # output이 될 아이들
        ques_header=0
        ques_content=0
        selected_ans_content=0
        keyword_list=[0]
        status=0

        # Request 부분
        try:
            status, soup=self.request_through_url(url)
        except Exception as ex:
            print('Exception in request_throught_url function')
            print(ex)
            return ques_header, ques_content, selected_ans_content, keyword_list

        # status 마다 어케 대처할지 생각해봐야할듯
        if status==200:
            pass
        elif status==100:
            # do something
            s=2
        else:
            s=2

        # Question header - 질문 제목 뜯기 ===============================
        try:
            ques_header=soup.find(attrs={'id': 'question-header'})
            ques_header=ques_header.find('h1')
        except Exception as ex:
            print('Exception in ques_header')
            print(ex)

        # get question contents - 질문 내용 & 이미지 ==============================
        try:
            ques_content1=soup.find(attrs={'class':'question'})
            ques_content=ques_content1.find(attrs={'class':'s-prose js-post-body'})
            if ques_content.find(attrs={'class':'s-notice s-notice__info post-notice js-post-notice mb16'}):
                ques_content.find(attrs={'class':'s-notice s-notice__info post-notice js-post-notice mb16'}).extract()

        except Exception as ex:
            print('Exception in ques_content')
            print(ex)


        # tag - 키워드 ========================================================
        try:
            keyword_html=soup.findAll(attrs={'class':'post-tag'})
            keyword_list=self.get_keyword(keyword_html)
        except Exception as ex:
            print('Exception in keyword scraping')
            print(ex)

        # get answer - 답변 ===============================================
        try:
            ans_container=soup.find(attrs={'id': 'answers'})
            selected_ans_container=self.select_answer(ans_container)
            selected_ans_content=selected_ans_container.find(attrs={'class' : 's-prose js-post-body'})

        except Exception as ex:
            print('Exception in answer_part')
            print(ex)


        # self.print_test_result(ques_header, ques_content, selected_ans_content, keyword_list)


        ques_header = ques_header.get_text()
        ques_content_str,selected_ans_content_str,ques_all_json = self.extract_tag(ques_header,str(ques_content),str(selected_ans_content))

        return ques_header, ques_content_str,selected_ans_content_str,ques_all_json, keyword_list, status

    # 불필요한 html 제거한 html들을 합치는 역할 (this question already has answers here) --미사용
    def merge_htmlarray(self, ques_content_arr):
        return ''.join(map(str, list(ques_content_arr)))

    # 키워드 크롤 함수
    def get_keyword(self, keyword_html):
        keyword_list=[]
        for key in keyword_html:
            keyword_list.append(key.text)
        keyword_list=list(dict.fromkeys(keyword_list))
        return keyword_list

    # 여러 답변 중 하나 선택하는 함수
    def select_answer(self, ans_container):

        # if there is no answer at all
        # --> 답변이 아예 없을 경우 대처 방안 :: ouptut null
        if not ans_container.find(attrs={'class' : 's-prose js-post-body'}):
            return 10000


        # if there is selected answer - accepted answer로 선택
        if ans_container.find(attrs={'class': 'answer js-answer accepted-answer'}):
            selected_ans_container=ans_container.find(attrs={'class': 'answer js-answer accepted-answer'})

        # bounty 주어진 답변 있으면 선택
        elif ans_container.find(attrs={'class' : 'js-bounty-award-container flex--item pb4'}):
            child=ans_container.find(attrs={'class' : 'js-bounty-award-container flex--item pb4'})
            selected_ans_container=child.parent.parent.parent.parent

        # No selected or bounty answer - 뭐도 없을 경우
        else:
            print('-----------currently no selected answer---------------')
            all_answers=ans_container.find_all(attrs={'class':'answer js-answer'})

            # select answer with max data-score - 가장 추천수가 높은 답변을 임의로 선택
            score_list=[]

            for (i, lst) in enumerate(all_answers):
                score_list.append(int(lst.attrs['data-score']))

            selected_ans_index=score_list.index(max(score_list))
            selected_ans_container=all_answers[selected_ans_index]

        return selected_ans_container

    # For Debugging
    def print_test_result(self, question, ques_detail, answer, keyword_list):

        print('================process done========================')
        print('\n----------Question Header-----------\n')
        print(question)
        print('\n----------Quesntion Contents--------\n')
        print(ques_detail)
        print('\n-------------Answer---------------\n')
        print(answer)
        print('\n-------------keywords---------------\n')
        print(keyword_list)


    def request_through_url(self, url):
        response=requests.get(url)
        if response.status_code==200:
            html=response.text
            soup=BeautifulSoup(html, 'html.parser')
            return response.status_code, soup

        else:
            print(response.status_code)
            return response.status_code, 0

    def extract_tag(self, header,text1, text2):

        html1 = str(text1)
        html2 = str(text2)

        body1 = re.findall('(?<=\<p>)(.*?)(?=<\/p>)|(?<=\<pre>)(.*?)(?=<\/pre>)', html1, re.I | re.S)
        body2 = re.findall('(?<=\<p>)(.*?)(?=<\/p>)|(?<=\<pre>)(.*?)(?=<\/pre>)', html2, re.I | re.S)

        id_ask =[]
        id_ans =[]
        text_ask=[]
        text_ans=[]

        ret=[]
        ret2 = []
        for i in body1:
            ret.append(list(i))
            if (i[0] == ""):
                # print("\n<code>")
                ret[-1][1] = re.sub('<.+?>', '', i[1], 0, re.I | re.S)
                ret[-1][0] = 1
                id_ask.append(1)
                text_ask.append(ret[-1][1])
                # print(ret[-1][1])
            else:
                # print("\n<paragraph>")
                ret[-1][1] = i[0]
                ret[-1][0] = 0

                id_ask.append(0)
                text_ask.append(ret[-1][1])

                # print(ret[-1][1])
        for i in body2:
            ret2.append(list(i))
            if (i[0] == ""):
                # print("\n<code>")
                ret2[-1][1] = re.sub('<.+?>', '', i[1], 0, re.I | re.S)
                ret2[-1][0] = 1
                # print(ret[-1][1])
                id_ans.append(1)
                text_ans.append(ret2[-1][1])
            else:
                # print("\n<paragraph>")
                ret2[-1][1] = i[0]
                ret2[-1][0] = 0
                # print(ret[-1][1])
                id_ans.append(0)
                text_ans.append(ret2[-1][1])

        ques_content_str=ret
        selected_ans_content_str=ret2

        #[[0,"paragraph"],[1,"code"]]

        somedict = {"header":{"header":header},
                    "id": {"ask":[x for x in id_ask],
                           "ans":[y for y in id_ans]
                           },
                    "text": {"ask": [x for x in text_ask],
                             "ans": [y for y in text_ans]
                        }
                    }


        somedict=json.dumps(somedict)
        return ques_content_str,selected_ans_content_str,somedict

        # return splited text : head/content(list)/answer(list)


    def get_total_text(self,ques_header, ques_content,selected_ans_content):
        str = ""
        str += ques_header + "."

        for i in ques_content:
            if i[0] == 0:
                str += i[1] + '.'
        for i in selected_ans_content:
            if i[0] == 0:
                str += i[1] + '.'

        # return self.summarization_KoBART(str)
        return str

    # 1xx : informational respone - continuing process 로오디잉중
    # 2xx : successful
    # 3xx : redirection - further action needs to be taken in order to complete the request
    # 4xx : client error - request contains bad syntax - 404는 not found
    # 5xx : server failed a apparently valid request


# 예시 페이지
# https://stackoverflow.com/questions/8546245/python-concat-string-with-list?noredirect=1&lq=1
# https://stackoverflow.com/questions/41596810/how-to-print-an-exception-in-python-3
# 'https://stackoverflow.com/questions/68024674/how-to-correctly-process-arguments-to-avoid-raising-an-exception?noredirect=1&lq=1'
# 'https://workplace.stackexchange.com/questions/184095/colleague-just-wont-let-things-go-it-wastes-time-and-affects-my-morale'
# 'https://ell.stackexchange.com/questions/313120/the-sentence-is-talking-about-a-candidate-and-an-election-why-does-it-use-t'
# 'https://physics.stackexchange.com/questions/702873/how-can-an-electron-be-a-point-particle-but-also-a-wavefunction'
# https://gis.stackexchange.com/questions/428642/how-to-detect-and-make-all-connected-lines-in-the-same-direction-in-qgis


# url='https://stackoverflow.com/questions/39885359/beautifulsoup-decompose'
# stack=Stackoverflow()
# ques_head, ques_content, answer, keyword_list, status=stack.stackOverflow_process(url)
