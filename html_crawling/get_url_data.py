from stackoverflow_process import *
from quora_html import *

from summarization_process import *

class get_url_data:
    def __init__(self):
        # call only for once (summarization) : time reduction
        self.summ = summarization()

    def text_for_one_url(self,url):
        self.url = url  # url link
        # self.url_kind #for url classify
        if "stackoverflow.com/questions" in self.url:
            self.process_class = stackOverFlow_process(self.url)
            self.url_kind = 1
        elif "quora.com/" in self.url:
            self.process_class = Quora()
            self.url_kind = 2
            self.q_title, _, self.q_ans_list, self.q_ans_total = self.process_class.quora_process(url)
        else:
            self.url_kind = 3

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
            return self.summ.get_summarization(self.process_class.get_total_text())
        elif self.url_kind==2:
            return self.summ.get_summarization(self.q_ans_total)
