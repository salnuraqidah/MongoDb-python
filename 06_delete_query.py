from pymongo import MongoClient

democlient = MongoClient()
myclient = MongoClient('localhost',27017)
mydb = myclient["demo"]      #db name
mycoll = mydb["dbtable"]     #collection name

myquery = {"address":{"$regex":"^S"}}
#myquery = {"name":"Sandy"}

#mydoc = mycoll.delete_one(myquery)
mydoc = mycoll.delete_many(myquery)

for x in mycoll.find():
    print(x)