from email.mime import application

from flask import Flask, jsonify, session, redirect, url_for, config
from flask import request as RRR
from flask_restx import Api, Resource
from flask_cors import CORS
#import urllib
from html_crawling.get_url_data import get_url_data
import json
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# db = SQLAlchemy(app)
# db.init_app(app)
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)
app.secret_key = "super secret key"
CORS(app)

connections={}
connections['object']=get_url_data()
connections['count']=0

# db.create_all()
# # Create our database modl
# class DataObject(db.Model):
#     """ User Model for storing user related details """
#     __tablename__ = "users"
#
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     name = db.Column(db.String(255), unique=True, nullable=False)
#     python_object = db.Column(db.PickleType(), nullable=True)
#
#
#     def __init__(self, name):
#         self.name = name
#
#     # create funciton to add python object
#     def add_python_object(self, object_to_store):
#         persistent_python_object = db.Column() # <-- would like to add python object here
#         self.persistent_python_object = object_to_store


@app.route('/ajax', methods=['POST'])
def ajax():
    data = RRR.get_json()
    #print(data)
    #print("ajax")
    #x=connections['object']
    connections['count']=connections['count']+1
    print(connections['count'])

    url=data['url']
    option1 = data["option2"]
    option2 = data["option2"]
    option3 = data["option3"]
    #option4 = data["option4"]

    connections['object'].text_for_one_url(str(url))

    res1 = data["option2"]
    res2 = data["option2"]
    res3 =  data["option2"]
    #res4 = None

    #일단 3은 하지 말자

    if option1 =='1':
        res1 = connections['object'].option(1)
        #json.dumps(res1)
    if option2 =='1':
        res2 = connections['object'].option(2)
        res2=json.dumps(res2)
    if option3 =='1':
        res3 = connections['object'].option(3)
        json.dumps(res3)
    # if option4 is not None:
    #     res4= x.option(4)
    #     #json.dumps(res4)

    #print(res2)
    return jsonify(result = "success", option1= res1,option2=res2,option3=res3)

@app.route('/',methods=['POST'])
def main():
    # if "init" not in session:
        #초기화 하지 않은 경우 (쿠키에서 삭제됨)
        #x = get_url_data().__dict__
        # session['init']="init"
        #session['object'] = get_url_data().__dict__
        #--------------------------
        # adder = DataObject('Adder')
        # adder.add_python_object(get_url_data())
        #
        # db.session.add(adder)
        # db.session.commit()
        #--------------------------


        # print("initialized")

    data=RRR.get_json()
    #option, url data 입력받아야함
    return redirect(url_for('ajax',data=data)) #/ajax로 이동

# class ModelEncoder( JSONEncoder ) :
#     def default( self , obj ) :
#         if isinstance( obj , Model ):
#             return obj.to_json()
#         # Let the base class default method raise the TypeError
#         return json.JSONEncoder.default( self , obj )

if __name__ == '__main__':

    app.run(debug=True)