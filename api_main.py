from flask import Flask, jsonify, abort, request, make_response, url_for
import json
import datetime
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient()
mongobase = client.workout

db={ 'serie1': 20,'serie2': 22 ,'serie3': 23 ,'serie4': 18 ,'serie5': 21,'id':14 }
db2={ 'serie1': 2,'serie2': 2 ,'serie3': 2 ,'serie4': 1 ,'serie5': 2,'id':14 }
usepost={ 'use': 14}
db8={ 'serie1': 1,'serie2': 2 ,'serie3': 3 ,'serie4': 18 ,'serie5': 21,'id':14 }



@app.route('/<user>', methods = ['GET'])
def get_tasks(user):
    if request.method == 'POST':
      return jsonify( db2 ),200
    else:
      x=mongobase.workout.find_one({'user':[user]})
      print(x)
      print(type(x))
      return str(x),200

@app.route('/add', methods = ['GET','POST'])
def get_data():
    if request.method == 'POST':
      id = request.args.get("id")
      name = request.args.get("name")
      db3={ 'id': id,'name': name }
      return jsonify( db3 ),200
    else:
      id = request.args.get("id")
      name = request.args.get("name")
      db4={ 'id': id,'name': 'yue' }
      return jsonify( db4 ),200
    
@app.route('/json', methods = ['GET','POST'])
def get_json():
      content = request
      print(content.json)
      x=str(datetime.datetime.now())
      with open('file_'+x+'.json', 'w') as f:
         json.dump(request.json, f)
      if request.json:
        mydata = request.json # will be 
        return jsonify( db ),200
      else:
        return jsonify( db8 ),200
        
@app.route('/try', methods = ['GET','POST'])
def get_try():
      content = request
      x=str(datetime.datetime.now())
      if request.json:
        mydata = request.json # will be 
        print(mydata)
        mongobase.workout.insert_one(dict(mydata))
        return jsonify( mydata ),200
      else:
        return jsonify( db8 ),200
    
        
if __name__ == '__main__':
    app.run("0.0.0.0",debug = True)
