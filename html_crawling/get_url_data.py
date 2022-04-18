from stackoverflow_process import *
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
            self.process_class = stackOverFlow_process(self.url)
            self.url_kind = 1
            self.text_all=self.process_class.get_total_text()
            self.lang=self.isKorean(self.text_all)
        elif "quora.com/" in self.url:
            self.process_class = Quora()
            self.url_kind = 2
            self.q_title, _, self.q_ans_list, self.q_ans_total = self.process_class.quora_process(url)
            self.text_all=self.q_title+self.q_ans_total
            self.lang = self.isKorean(self.text_all)
        else:
            self.url_kind = 3
            #self.text_all
            self.lang = self.isKorean(self.text_all)

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
        if self.url_kind==1:
            all_head,all_content,all_answer=self.process_class.get_all()
            return all_head,all_content,all_answer #[[0,"paragraph"],[1,"code"]]
        elif self.url_kind==2:
            return self.q_ans_list

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
