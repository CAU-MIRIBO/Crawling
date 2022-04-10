from get_url_data import *
from summarization_process import *

# call only for once (summarization) : time reduction
summ=summarization()


# for each url
x=get_url_data("https://stackoverflow.com/questions/2612548/extracting-an-attribute-value-with-beautifulsoup")
# Option Request Reply
# 1 - keyword
# 2 - summarization
# 3 - sentance
# 4 - show all
print(x.option(4))
# get total text from get_url_data class => send to summarization class and summarize
print(summ.get_summarization(x.option(2)))

