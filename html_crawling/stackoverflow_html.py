from urllib import request
import requests
from bs4 import BeautifulSoup

url='https://stackoverflow.com/questions/133698/why-does-fatal-error-lnk1104-cannot-open-file-c-program-obj-occur-when-i-c'

def stackOverflow_process(soup):
    # print(soup)
    
    ques_header=soup.find_all(attrs={'id': 'question-header'})
    ques=ques_header[0].text
    
    ques_contents=soup.find_all(attrs={'class':'s-prose js-post-body'})
    ques_text=ques_contents=ques_contents[0].text
    
    answer_child=soup.find_all(attrs={'class': 'js-accepted-answer-indicator flex--item fc-green-500 py6 mtn8'})[0]
    answer_parent1=answer_child.parent.parent.parent

    answer_field=answer_parent1.find_all(attrs={'class' : 's-prose js-post-body'})
    answer_text=answer_field[0].text
    
    
    # print(ques_text)
    # print(soup.text)
    return ques, ques_text, answer_text

response=requests.get(url)
if response.status_code==200:
    html=response.text
    soup=BeautifulSoup(html, 'html.parser')
    question, ques_detail, answer=stackOverflow_process(soup)
    
else:
    print(response.status_code)
    

print('================process done========================')
print('-----Question-----------')
print(question)
print(ques_detail)
print('-------------answer---------------')
print(answer)


    