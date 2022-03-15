from urllib import request
import requests
from bs4 import BeautifulSoup

url='https://www.nbcnews.com/news/us-news/jamal-edwards-music-entrepreneur-helped-launch-ed-sheeran-jessie-j-die-rcna17041'

response=requests.get(url)

if response.status_code==200:
    html=response.text
    soup=BeautifulSoup(html, 'html.parser')
    print(soup)
    
else:
    print(response.status_code)
    

print('process done')