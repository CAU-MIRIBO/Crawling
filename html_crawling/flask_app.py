from flask import Flask, jsonify
from flask import request as RRR
from flask_restx import Api, Resource
from flask_cors import CORS
#import urllib
from html_crawling.get_url_data import get_url_data

app = Flask(__name__)
api = Api(app)
CORS(app)

# @app.route("/start",methods=["POST",'GET'])
# def start():
#     if requst.


@app.route("/option2",methods=['POST','GET'])
def option2():
    url=""
    if RRR.method == 'POST':
        url=RRR.form

        x = get_url_data()
        x.text_for_one_url(str(url))
    #print(x.option(2))
    return str(x.option(2))


@app.route('/ajax', methods=['POST'])
def ajax():
    data = RRR.get_json()
    print(data)
    x = get_url_data()
    url=data['url']
    x.text_for_one_url(str(url))
    res2=x.option(4)
    print(res2)
    return jsonify(result = "success", result2= res2)


if __name__ == '__main__':
    app.run(debug=True)