from pymongo import MongoClient

democlient = MongoClient()
myclient = MongoClient('localhost',27017)
mydb = myclient["demo"]      #db name
mycoll = mydb["dbtable"]     #collection name

#myquery = {"name":"John"}            #normal query
#myquery = {"name":{"$regex":"^S"}}   #query search using regex
myquery = {"address":{"$regex":"^S"}}   #query search using regex


mydoc = mycoll.find(myquery)
for x in mydoc:
    print(x)
