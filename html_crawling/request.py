from get_url_data import *
import pprint


# call only for once : time reduction <-summarization
from html_crawling.get_url_data import get_url_data

x=get_url_data()

#for one url
# x.text_for_one_url("https://www.quora.com/How-is-the-culture-of-Jeju-Island-different-from-the-rest-of-South-Korea")
# Option Request Reply
# 1 - keyword
# 2 - summarization
# 3 - sentance
# 4 - show all
# print("----stackoverflow option 4----")
# pprint.pprint(type(x.option(4)))
# get total text from get_url_data class => send to summarization class and summarize
# print("\n----stackoverflow option 2----")
# print(x.option(2))
# print("\n----stackoverflow option 1----")
# print((x.option(1)))

list=['https://www.quora.com/How-is-the-culture-of-Jeju-Island-different-from-the-rest-of-South-Korea',
      'https://www.hani.co.kr/arti/culture/culture_general/1023318.html',
      'https://moviesnmore.quora.com/What-will-be-the-best-movie-of-2021-4',
      'https://developer.mozilla.org/en-US/docs/Web/API/Element/remove',
      'https://blog.naver.com/maximusc/222698515250',
      'https://overseas.mofa.go.kr/ae-dubai-ko/brd/m_10772/view.do?seq=1342548',
      'https://kin.naver.com/qna/detail.naver?d1id=6&dirId=6010102&docId=418095586&qb=7J6Q6rCA6rKp66as&enc=utf8&section=kin.ext&rank=1&search_sort=0&spq=0',
      'https://www.facebook.com/GameOfThrones/',
      'https://twitter.com/HouseofDragon/status/1509193733585076228?cxt=HHwWiICsuYzt3fEpAAAA', #얘 안됨
      'https://namu.wiki/w/Hades(%EA%B2%8C%EC%9E%84)',
      'http://cau.ac.kr/~bongbong/multicore22/',
      'https://dojang.io/mod/page/view.php?id=2372'
      ]




for i in list:
    x.text_for_one_url(i)
    print(i)
    print(x.option(1))
    print(x.option(2))
    print('\n')

# x.text_for_one_url("https://www.quora.com/What-are-some-facts-about-Spider-man-that-are-beyond-amazing")
# print("\n----stackoverflow option 2----")
# print(x.option(2))
# print("\n----stackoverflow option 1----")
# print((x.option(1)))
#
# print("\n\n++++++++++++++++++++quora+++++++++++++++++++++")
# x.text_for_one_url('https://moviesnmore.quora.com/What-will-be-the-best-movie-of-2021-4')
# # print("----quora option 4----")
# # pprint.pprint(x.option(4))
# print("\n----quora option 2----")
# print(x.option(2))
# print("\n----quora option 1----")
# print(x.option(1))
#
# x.text_for_one_url('https://eduhope88.tistory.com/494')
# print(x.option(2))
# x.text_for_one_url('https://eduhope88.tistory.com/485?category=412380')
# print(x.option(2))

# x.text_for_one_url('https://gis.stackexchange.com/questions/428642/how-to-detect-and-make-all-connected-lines-in-the-same-direction-in-qgis')
# print(x.option(4))