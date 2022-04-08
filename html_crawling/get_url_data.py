from stackoverflow_process import *

class get_url_data:
    def __init__(self,url):
        self.url=url  #url link
        if "stackoverflow.com/questions" in self.url:
            self.sp=stackOverFlow_process(self.url)

    def option(self,num):
        if num==1:
            return self.run_keyword()
        elif num==2:
            return self.run_summarization()
        elif num==3:
            return self.run_sentance()
        elif num==4:
            return self.run_all()

    def run_all(self):
        if "stackoverflow.com/questions" in self.url:
            self.all_head,self.all_content,self.all_answer=self.sp.get_all()

        return self.all_head,self.all_content,self.all_answer #[[0,"paragraph"],[1,"code"]]




x=get_url_data("https://stackoverflow.com/questions/2612548/extracting-an-attribute-value-with-beautifulsoup")
print(x.option(4))