from get_url_data import *


# call only for once : time reduction <-summarization
x=get_url_data()

#for one url
#x.text_for_one_url("https://stackoverflow.com/questions/2612548/extracting-an-attribute-value-with-beautifulsoup")
# Option Request Reply
# 1 - keyword
# 2 - summarization
# 3 - sentance
# 4 - show all
# print("----stackoverflow option 4----")
# print(x.option(4))
# # get total text from get_url_data class => send to summarization class and summarize
# print("\n----stackoverflow option 2----")
# print(x.option(2))


print("\n\n++++++++++++++++++++quora+++++++++++++++++++++")
x.text_for_one_url('https://moviesnmore.quora.com/What-will-be-the-best-movie-of-2021-4')
print("----quora option 4----")
print(x.option(4))
print("\n----quora option 2----")
print(x.option(2))
print("\n----quora option 1----")
print(x.option(1))

# x.text_for_one_url('https://gis.stackexchange.com/questions/428642/how-to-detect-and-make-all-connected-lines-in-the-same-direction-in-qgis')
# print(x.option(4))