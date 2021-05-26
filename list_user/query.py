from flask import Flask, request, jsonify, render_template
import pymongo
import json
import database
import sys

#database part
app = Flask(__name__)
db_add = "mongodb://10.128.0.5:27018/"


@app.route('/',methods=['GET'])
def entry_point():
    data_ = database.main(db_add)
    return  jsonify(data_)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001,debug=True)
