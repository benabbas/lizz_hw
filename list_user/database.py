import pymongo
import json

def db_all(mycol):
    db_list = []
    for x in mycol.find():
        data = str(x).replace("ObjectId(","")
        data = data.replace(")","")
        data = data.replace("'",'"')
        data = data.replace('"data": "{','')
        data = data.replace('}"','')
        db_list.append(json.loads(data))
    return db_list

def main(db_add):
    #database part
    db_add = "mongodb://10.128.0.5:27018/"
    myclient = pymongo.MongoClient(db_add)
    mydb = myclient["mydatabase"]
    mycol = mydb["key"]
    return db_all(mycol)
