from urllib import request
import requests
from bs4 import BeautifulSoup

url='https://stackoverflow.com/questions/133698/why-does-fatal-error-lnk1104-cannot-open-file-c-program-obj-occur-when-i-c'

response=requests.get(url)

if response.status_code==200:
    html=response.text
    soup=BeautifulSoup(html, 'html.parser')
    print(soup)
    
else:
    print(response.status_code)
    

print('process done')