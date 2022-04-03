from stackoverflow_process import *

class get_url_data:
    def __init__(self,url,code):
        self.url=url  #url link
        self.code=code # 1) hashtag,summary 2)

    def run_code(self):
        if "stackoverflow.com/questions" in self.url:
            sp=stackOverFlow_process(self.url)
            info_head,info_content,info_answer=sp.get_info()
            print(info_head)
            print(info_content)
            print(info_answer)

x=get_url_data("https://stackoverflow.com/questions/2612548/extracting-an-attribute-value-with-beautifulsoup",1)
x.run_code()