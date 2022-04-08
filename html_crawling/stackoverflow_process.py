from html_crawling import stackoverflow_html
import re
import torch
from transformers import PreTrainedTokenizerFast, BartForConditionalGeneration
from gensim.summarization.summarizer import summarize
from newspaper import Article


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
        self.processed_head = self.ques_head.get_text()
        self.processed_content = self.extract_tag(str(self.ques_content))
        self.processed_answer = self.extract_tag(str(self.answer))

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
                ret[-1][0]=1
                #print(ret[-1][1])
            else:
                #print("\n<paragraph>")
                ret[-1][1]=i[0]
                ret[-1][0]=0
                #print(ret[-1][1])

        return ret

    def get_all(self):
        return self.processed_head,self.processed_content,self.processed_answer

    def get_summarization(self):
        str = ""
        str += self.processed_head + "."

        for i in self.processed_content:
            if i[0]==0:
                str+=i[1]+'.'
        for i in self.processed_answer:
            if i[0] == 0:
                str += i[1]+'.'

        #return self.summarization_KoBART(str)
        return self.summarization_newspaper(str)

    def summarization_KoBART(self,text):
        self.tokenizer = PreTrainedTokenizerFast.from_pretrained('digit82/kobart-summarization')
        self.model = BartForConditionalGeneration.from_pretrained('digit82/kobart-summarization')
        #print(text)
        raw_input_ids = self.tokenizer.encode(text)
        input_ids = [self.tokenizer.bos_token_id] + raw_input_ids + [self.tokenizer.eos_token_id]
        summary_ids = self.model.generate(torch.tensor([input_ids]), num_beams=4, max_length=512, eos_token_id=1)
        return self.tokenizer.decode(summary_ids.squeeze().tolist(), skip_special_tokens=True)

    def summarization_newspaper(self,text):
        return summarize(text)