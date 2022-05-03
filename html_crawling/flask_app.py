from flask import Flask
from flask import request as RRR
from flask_restx import Api, Resource
#import urllib
from html_crawling.get_url_data import get_url_data

app = Flask(__name__)
api = Api(app)

# @app.route("/start",methods=["POST",'GET'])
# def start():
#     if requst.


@app.route("/option2",methods=['POS','GET'])
def option2():
    url =RRR.args.get("url")
    x = get_url_data()
    x.text_for_one_url(str(url))
    #print(x.option(2))
    return str(x.option(2))



if __name__ == '__main__':
    app.run(debug=True)