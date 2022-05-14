from general_website_html import Default

# 5/14 ver

url='https://www.ajunews.com/view/20211215155407703'
# url='https://www.quora.com/How-is-the-culture-of-Jeju-Island-different-from-the-rest-of-South-Korea'
# url='https://www.hani.co.kr/arti/culture/culture_general/1023318.html'
# url ='https://moviesnmore.quora.com/What-will-be-the-best-movie-of-2021-4'
# url='https://owl.purdue.edu/owl/subject_specific_writing/journalism_and_journalistic_writing/writing_leads.html'
# url='https://developer.mozilla.org/en-US/docs/Web/API/Element/remove' # 이거이거 문제가 있네
# url='https://blog.naver.com/maximusc/222698515250' # selenium 으로도 안됨....
# url='https://blog.naver.com/tmddlf/222700811326' # 네이버 블로그 전체적으로 작동 어려움
# url='https://overseas.mofa.go.kr/ae-dubai-ko/brd/m_10772/view.do?seq=1342548'  #자가격리 잘 돌아간다
# url='https://kin.naver.com/qna/detail.naver?d1id=6&dirId=6010102&docId=418095586&qb=7J6Q6rCA6rKp66as&enc=utf8&section=kin.ext&rank=1&search_sort=0&spq=0'
# url='https://newsis.com/view/?id=NISX20220428_0001851291&cID=10401&pID=10400'
# url='https://newsis.com/view/?id=NISX20220428_0001851291&cID=10401&pID=10400'
# url='https://edition.cnn.com/2022/04/28/tech/elon-musk-twitter-leadership/index.html'
# url='https://www.seoul.co.kr/news/newsView.php?id=20220502001007&wlog_sub=svt_006'
# url='https://sports.news.naver.com/news?oid=109&aid=0004605358'
# url='https://blog.naver.com/tngo1005/222717248571'
# url='https://section.blog.naver.com/OfficialBlog.naver?currentPage=1'
# url='https://www.google.com/search?q=python+replace&oq=spython+replace&aqs=chrome.1.69i57j0i13l9.5410j0j4&sourceid=chrome&ie=UTF-8'
# url='https://en.wikipedia.org/wiki/Game_of_Thrones'
# url='https://www.rottentomatoes.com/tv/game_of_thrones'
# url='https://brooklyn99.fandom.com/wiki/Raymond_Holt'
# url='https://www.facebook.com/GameOfThrones/'         # 페북 안됨
# url='https://www.rottentomatoes.com/tv/game_of_thrones'
# url='http://cau.ac.kr/~bongbong/multicore22/'
# url='https://twitter.com/HouseofDragon/status/1509193733585076228?cxt=HHwWiICsuYzt3fEpAAAA'

# 여기서부터 시작
url='https://namu.wiki/w/Hades(%EA%B2%8C%EC%9E%84)'  # 나무위키 안돌아가..
url='https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=kaiba1004&logNo=221747294637'  # newspaper 모듈로 크롤링 됨
url='https://www.gameinn.co.kr/news/articleView.html?idxno=1535' # newspaper로 크롤링
url='https://www.disneyplus.com/ko-kr/series/wandavision/4SrN28ZjDLwH' # 안돌아가
url='https://ko.wikipedia.org/wiki/%EB%8F%99%EB%AC%BC' # 동물 위키피디아 되기는 한다만... selenium으로
url='https://www.etoday.co.kr/news/view/2131371' # newspaper 모듈로
url='https://www.tutorialspoint.com/use-a-list-of-values-to-select-rows-from-a-pandas-dataframe' # newspaper 모듈로
url='https://ncv.kdca.go.kr/menu.es?mid=a30400000000' # 코로나 자가격리 규정
url='https://moviesnmore.quora.com/What-will-be-the-best-movie-of-2021-4' # 놀랍게도 잘 돌아간다..!
url='https://www.ekn.kr/web/view.php?key=20220414010002380' # newspaper module로
url='https://www.geeksforgeeks.org/python-classes-and-objects/' # geeksforgeeks는 newspaper 모듈로 돌아가는듯
url='https://kkoseul.tistory.com/58'   # tistory도 newspaper 모듈로 돌아간다!
url='https://docs.python.org/ko/3/howto/unicode.html' # docs.python.org 여기도 돌아간다!! newspaper module로
url='https://wikidocs.net/134567'  # wikidocs.net 도 newspaper module로 돌아간다
url='https://digiconfactory.tistory.com/entry/%EC%9C%A0%EB%8B%88%EC%BD%94%EB%93%9C%EC%99%80-%ED%95%9C%EA%B8%80-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9C%A0%EB%8B%88%EC%BD%94%EB%93%9C-%EC%B6%9C%EB%A0%A5%ED%95%98%EA%B8%B0-%ED%95%9C%EA%B8%80-%EA%B9%A8%EC%A7%80%EB%8A%94-%EB%AC%B8%EC%A0%9C-%ED%95%B4%EA%B2%B0%EB%B0%A9%EB%B2%95'
url='https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=vslinux&logNo=220599500768' # 네이버도 되는 경우도 있네?? # newspaper 갓..!
url='https://namu.wiki/w/%EC%99%84%EB%8B%A4%EB%B9%84%EC%A0%84' # 나무위키는 안돌아가...
url='https://dojang.io/mod/page/view.php?id=2372' # 코딩 도장 된다 newspaper 모듈
url='http://cau.ac.kr/~bongbong/multicore22/' # 봉봉 사이트는 안된다
url='https://cainstorm.com/162' # newspaper 모드
url='https://velog.io/@zionhann/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9C%A0%EB%8B%88%EC%BD%94%EB%93%9C-%EB%AC%B8%EC%9E%90-%EB%B3%80%ED%99%98%ED%95%98%EA%B8%B0'
# velog도 된다
url='https://velog.io/@dlwocks31/translation-project-management-at-big-tech'
# url='https://velog.io/@junh0328/%ED%94%84%EB%A1%A0%ED%8A%B8-%EC%97%94%EB%93%9C-%EB%A9%B4%EC%A0%91-%EC%A4%80%EB%B9%84-%ED%95%98%EC%8B%A4%EB%B6%84'
# 이건 셀레니움으로 들어가기는 하는데 되긴함 - 이 웹사이트느 안들어가는걸루
# url='https://velog.io/@jay/elon-musk-dont-follow-the-trend'

# tt, ti, hapy=arti.crawl_article_lastchance(url)
# arti.crawl_general_concept(url)
# a, b, c=arti.crawl_article_newspaper_mod(url)
# arti.crawling_article(url)
# title, contents=request_through_url(url)

arti=Default()
status, title, para, content_all=arti.general_website_process(url)
arti.print_test_result(title, para)