# !flask/bin/python
from flask import Flask, jsonify,request
import json

app = Flask(__name__)

@app.route('/getdata', methods=['GET'])
def get_tasks():
  with open('./data/Preds.json') as f:
    preds = json.load(f)
  preds = preds[0]
  return jsonify(preds)

@app.route('/data', methods=['GET'])
def get_query_string():  
  fileName =  request.args.get('file')
  with open('./data/'+ fileName +'.json') as f:
    myData = json.load(f)
  myData = myData[0]
  return jsonify(myData)
    

if __name__ == '__main__':
    app.run(debug=True)