from html_crawling import stackoverflow_html
from bs4 import BeautifulSoup as bs
import re

url='https://stackoverflow.com/questions/2612548/extracting-an-attribute-value-with-beautifulsoup'
#ques_head, ques_content, answer=stackoverflow_html.request_through_url(url)

# result_head=ques_head.get_text()
# print(result_head)
# result_content=ques_content.get_text()
# print(result_content)
#result_answer=answer.get_text()
#print(result_answer)
# soup=bs(str(answer),'html.parser')
# attr=soup.find_all('pre')
# for i in attr:
#     print(i.string)

class stackOverFlow_process:
    def __init__(self, url):
        self.url=url
        self.ques_head, self.ques_content, self.answer = stackoverflow_html.request_through_url(url)

    def extract_tag(self,html):
        html1=str(html)
        random_dict=dict()
        #result=html1.split('<(.+?)>')
        #p=re.sub('<.+?>','',html1,0,re.I|re.S)
        #print(p)
        # matches=r"(<p.*/p>) (<pre.*/pre>)"
        body=re.findall('(?<=\<p>)(.*?)(?=<\/p>)|(?<=\<pre>)(.*?)(?=<\/pre>)',html1,re.I|re.S)
        #print(type(body)) #list
        #body=body.group(0)
        #print(body)
        # p = re.compile('(?<=\<p>)(.*?)(?=<\/p>)|(?<=\<pre>)(.*?)(?=<\/pre>)')
        # p_tag_list = p.findall(html1)
        # print(p_tag_list)

        # for i in range(len(html1)):
        #     print(html[i])

        ret=[]
        for i in body:
            ret.append(list(i))
            if(i[0]==""):
                #print("\n<code>")
                ret[-1][1]=re.sub('<.+?>', '', i[1], 0, re.I|re.S)
                ret[-1][0]='code'
                #print(ret[-1][1])
            else:
                #print("\n<paragraph>")
                ret[-1][1]=i[0]
                ret[-1][0]='paragraph'
                #print(ret[-1][1])

        print(type(ret[0]))
        return ret

    def get_info(self):
        self.processed_head=self.ques_head.get_text()
        self.processed_content=self.extract_tag(str(self.ques_content))
        self.processed_answer=self.extract_tag(str(self.answer))


