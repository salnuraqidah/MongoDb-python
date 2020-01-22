from pymongo import MongoClient

democlient = MongoClient()
myclient = MongoClient('localhost',27017)
mydb = myclient["demo"]      #db name
mycoll = mydb["dbtable"]     #collection name

# mycoll.drop()                        #drop collection
# democlient.drop_database("demo")     #drop db
# print(myclient.list_database_names())

# myquery = {"name":"Betty"}
# newvalues = {"$set": {"name":"Cala"}}

myquery = {"address": {"$regex":"^S"}}
newvalues = {"$set": {"address":"Mansion Street 105"}}

# mycoll.update_one(myquery, newvalues)
mycoll.update_many(myquery, newvalues)

for x in mycoll.find().limit(4):
    print(x)