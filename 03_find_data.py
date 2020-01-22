from pymongo import MongoClient

democlient = MongoClient()
myclient = MongoClient('localhost',27017)
mydb = myclient["demo"]      #db name
mycoll = mydb["dbtable"]     #collection name

#x = mycoll.find_one()
for x in mycoll.find():
    print(x)