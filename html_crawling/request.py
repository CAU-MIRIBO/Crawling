from get_url_data import *
from summarization_process import *


x=get_url_data("https://stackoverflow.com/questions/2612548/extracting-an-attribute-value-with-beautifulsoup")
print(x.option(4))
print(x.option(2))