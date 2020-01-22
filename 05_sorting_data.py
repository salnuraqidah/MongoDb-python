from pymongo import MongoClient

democlient = MongoClient()
myclient = MongoClient('localhost',27017)
mydb = myclient["demo"]      #db name
mycoll = mydb["dbtable"]     #collection name

mydoc = mycoll.find().sort('name',1) #ascending
#mydoc = mycoll.find().sort('name',-1) #descending

for x in mydoc:
    print(x)