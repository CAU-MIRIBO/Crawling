from stackoverflow_html import *
from quora_html import *

from summarization_process import *
from konlpy.tag import Okt
okt=Okt()

from keyword_process import *
import re

class get_url_data:
    def __init__(self):
        # call only for once (summarization) : time reduction
        self.summ = summarization()

    def text_for_one_url(self,url):
        self.url = url  # url link
        # self.url_kind #for url classify
        if "stack" in self.url:
            self.process_class = Stackoverflow()
            self.url_kind = 1
            ques_header, ques_content,selected_ans_content,keyword_list, status=self.process_class.stackOverflow_process(url)
            self.text_all =self.process_class.get_total_text(ques_header,ques_content,selected_ans_content)
            self.lang=self.isKorean(self.text_all)
        elif "quora.com/" in self.url:
            self.process_class = Quora()
            self.url_kind = 2
            quo_ques, quo_ques_cont, quo_answer_list, quo_full_answer, status= self.process_class.quora_process(url)
            self.text_all=str(quo_ques)+'\n'+str(quo_full_answer)
            self.lang = self.isKorean(self.text_all)
        else:
            self.url_kind = 3
            #self.text_all
            self.lang = self.isKorean(self.text_all)

        if status==0:
            print("")
            #error
            #나중에 하기

    def isKorean(self,text):
        hangul = re.compile('[\u3131-\u3163\uac00-\ud7a3]+')
        result = hangul.findall(text)
        if len(result)>0 :
            return 'kr'
        else:
            return 'en'

    def option(self,num):
        if num==1:
            return self.run_keyword()
        elif num==2:
            return self.run_summarization()
        elif num==3:
            return self.run_sentance()
        elif num==4:
            return self.run_all()

    #all text to show user
    def run_all(self):
        return self.text_all

    #return all combined text to run summarization outside
    def run_summarization(self):
        if self.url_kind==1:
            return self.summ.get_summarization(self.text_all)
        elif self.url_kind==2:
            return self.summ.get_summarization(self.text_all)


    def run_keyword(self):
        if self.url_kind==1:
            return keyword_extractor('yake',self.lang, self.text_all)
        elif self.url_kind==2:
            return keyword_extractor('yake',self.lang, self.text_all)
