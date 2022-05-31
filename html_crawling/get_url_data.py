import json

from konlpy.tag import Okt

from quora_html import Quora
from stackoverflow_html import Stackoverflow
from summarization_process import summarization
from general_website_html import Default
import sys
okt=Okt()

from html_crawling.keyword_process import *
import re

class get_url_data:
    def __init__(self):
        # call only for once (summarization) : time reduction
        self.summ = summarization()
        #self.err=False

    def text_for_one_url(self,url):
        self.url = url  # url link
        # self.url_kind #for url classify
        self.err=False
        status=200
        if "stackoverflow.com/questions" in self.url:
            self.process_class = Stackoverflow()
            self.url_kind = 1
            self.ques_header, self.ques_content_str,self.selected_ans_content_str,self.ques_all_json, self.keyword_list, status=self.process_class.stackOverflow_process(url)
            if status!=0:
                self.text_all =self.process_class.get_total_text(self.ques_header, self.ques_content_str,
                                                                 self.selected_ans_content_str)
                self.lang=self.isKorean(self.text_all)
        elif "quora.com/" in self.url:
            self.process_class = Quora()
            self.url_kind = 2
            quo_ques, quo_ques_cont, quo_answer_list, quo_full_answer, status= self.process_class.quora_process(url)
            self.text_all=str(quo_ques)+'\n'+str(quo_full_answer)
            self.lang = self.isKorean(self.text_all)
        else:
            try:
                self.process_class=Default()
                self.url_kind = 3
                status, title, para, content_all = self.process_class.general_website_process(url)
                #self.text_all
                self.text_all=title + '\n'+content_all
                self.lang = self.isKorean(self.text_all)
            except:
                #error
                #sys.exit()
                print("else_ try except")
                status=0
                self.err=True

        if status==0:
            print("status:0")
            #error
            #나중에 하기
            self.err=True

    def isErr(self):
        return self.err

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
            #stackoverflow 사이트 예외
            if self.url_kind==1 and len(self.keyword_list)!=0:
                return self.stack_run_summarization()
            return self.run_summarization()
        # elif num==3:
        #     return self.run_sentance()
        # elif num==4:
        #     return self.run_all()

    #all text to show user
    def run_all(self):
        return self.text_all

    def stack_run_summarization(self):
        return self.ques_all_json

    #return all combined text to run summarization outside
    def run_summarization(self):
        if self.url_kind==1:
            return self.summ.get_summarization(self.text_all,self.lang)
        elif self.url_kind==2:
            return self.summ.get_summarization(self.text_all,self.lang)
        else:
            return self.summ.get_summarization(self.text_all,self.lang)

    def run_keyword(self):
        if self.url_kind==1:
            #return keyword_extractor('yake',self.lang, self.text_all)
            return self.keyword_to_dict(self.keyword_list)
        elif self.url_kind==2:
            list=keyword_extractor('yake',self.lang, self.text_all)
            return self.keyword_to_dict(list)
        else:
            list = keyword_extractor('yake', self.lang, self.text_all)
            return self.keyword_to_dict(list)

    def keyword_to_dict(self,list):
        somedict = {"keywords": [x for x in list],
                    }
        somedict = json.dumps(somedict)
        return somedict