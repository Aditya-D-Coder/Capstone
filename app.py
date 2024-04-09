from flask import Flask, jsonify

app = Flask(__name__)

people =[
    {'id':1,'name':'raju','num':2344},
    {'id':2,'name':'jay','num':76554}]
@app.get('/name')
def hello_world():
    return jsonify(people)
