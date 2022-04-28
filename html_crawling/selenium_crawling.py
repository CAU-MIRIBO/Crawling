import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def request_with_selenium(Url):
    
    options = webdriver.ChromeOptions()
    
    # # 창 사이즈
    # options.add_argument('window-size=1920,1080')  
    
    # 창 띄우지 않기
    options.add_argument('headless') 
     
    # Apply options
    driver = webdriver.Chrome(executable_path='C:\\Users\\hjson\\Downloads\\chromedriver.exe')
    # driver.implicitly_wait(3)
    
    driver.get(Url)
    print(driver.current_url)
    
    # 페이지 내에서 값 읽어오기
    head=driver.find_element_by_tag_name('head')
    body=driver.find_element_by_tag_name('body')
    
    head_src=head.get_attribute('innerHTML')
    body_src=body.get_attribute('innerHTML')
    
    # driver.close() --> driver 닫혀도 되나?
    driver.close()
    return head_src, body_src
    
    # driver.implicitly_wait(time_to_wait=5)
    
def request_with_selenium_raw(Url):
    
    options = webdriver.ChromeOptions()
    
    # # 창 사이즈
    # options.add_argument('window-size=1920,1080')  
    
    # 창 띄우지 않기
    options.add_argument('headless')
     
    # Apply options
    driver = webdriver.Chrome(executable_path='C:\\Users\\hjson\\Downloads\\chromedriver.exe')
    # driver.implicitly_wait(3)
    
    driver.get(Url)
    print(driver.current_url)
    
    # 페이지 내에서 값 읽어오기
    head=driver.find_element_by_tag_name('head')
    body=driver.find_element_by_tag_name('body')
    
    # head_src=head.get_attribute('innerHTML')
    # body_src=body.get_attribute('innerHTML')
    
    # driver.close() --> driver 닫혀도 되나?
    
    return head, body, driver
        
def print_test_result(title, contents):
    
    print('================process done========================')
    print('\n----------Title-----------\n')
    print(title)
    print('\n-------------Content---------------\n')
    print(contents)
    print('\n')
    
url='https://www.quora.com/How-is-the-culture-of-Jeju-Island-different-from-the-rest-of-South-Korea'
# 'https://www.hani.co.kr/arti/culture/culture_general/1023318.html'
# 'https://www.ajunews.com/view/20211215155407703'

# print_test_result(title,contents)

# request_with_selenium(url)