import lxml.html
import lxml.html.clean

class Parser(object):
    
    @classmethod
    def clean_article_html(cls, node):
        article_cleaner = lxml.html.clean.Cleaner()
        article_cleaner.javascript = True
        article_cleaner.style = True
        article_cleaner.allow_tags = [
            'a', 'span', 'p', 'br', 'strong', 'b',
            'em', 'i', 'tt', 'code', 'pre', 'blockquote', 'img', 'h1',
            'h2', 'h3', 'h4', 'h5', 'h6',
            'ul', 'ol', 'li', 'dl', 'dt', 'dd']
        article_cleaner.remove_unknown_tags = False
        return article_cleaner.clean_html(node)