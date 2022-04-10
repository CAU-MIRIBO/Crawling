from stackoverflow_process import *
from quora_process import *


class get_url_data:
    def __init__(self,url):
        self.url=url  #url link

        if "stackoverflow.com/questions" in self.url:
            self.sp=stackOverFlow_process(self.url) #already pro
        elif "quora.com" in self.url:
            self.qp=quora_process(self.url)

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
        if "stackoverflow.com/questions" in self.url:
            all_head,all_content,all_answer=self.sp.get_all()
            return all_head,all_content,all_answer #[[0,"paragraph"],[1,"code"]]

    #return all combined text to run summarization outside
    def run_summarization(self):
        if "stackoverflow.com/questions" in self.url:
            return self.sp.get_total_text()
