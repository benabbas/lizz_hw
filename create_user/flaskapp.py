from flask import Flask, request, jsonify
import os
import publisher
import pymongo
import json

#Flask Part
app = Flask(__name__)
data = {"key":"this is default"}

#database part
myclient = pymongo.MongoClient("mongodb://10.128.0.5:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["key"]


@app.route('/',methods=['GET','POST'])
def entry_point():
    data = request.get_json() #this part is fect the value from the body
    result = publisher.publisher(data['key'])
    return {"message" : "success "+result}

@app.route('/getdb', methods=['GET'])
def get_db():
    return jsonify(db_all())

def db_all():
    db_list = []
    for x in mycol.find():
        data = str(x).replace("ObjectId(","")
        data = data.replace(")","")
        data = data.replace("'",'"')
        db_list.append(json.loads(data))

    return db_list

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
    

