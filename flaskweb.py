import flask
import os

from flask import request, jsonify, make_response, render_template
from flask import Flask

app = Flask(__name__)

Data = {}

Data['1'] = {
    "Name":"Prasad",
    "Age":20
    }

Data['2'] = {
    "Name":"PSPK",
    "Age":49
    }

@app.route('/',methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/all',methods=['GET'])
def display():
    return jsonify(Data)

@app.route('/data/<obj>',methods=['GET'])
def display_part(obj):
    if obj in Data:
        res = make_response(jsonify(Data[obj]),200)
        return res
    else:
        res = make_response(jsonify({"Error":"Object not found"}),404)
        return res

@app.route('/data/update/<obj>',methods=['PATCH'])
def patch(obj):
    req = request.get_json
    if obj in Data:
        for k,v in req.items():
            Data[obj][k]=v
        res = make_response(jsonify({"Success":"Value Updated"}),200)
        return res
    else:
        Data[obj] = req
        res = make_response(jsonify({"Created":"Object Created"}),200)
        return res
        
        

if __name__=="__main__":
    app.run()
