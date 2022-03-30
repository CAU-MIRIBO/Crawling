from newspaper import Article

url='https://www.etnews.com/20220304000171?mc=ns_003_00001'

article=Article(url)
article.download()

print(article.html)

article.parse()
print(article.authors)
print(article.publish_date)
print(article.text)

print(article.keywords)
print(article.summary)

