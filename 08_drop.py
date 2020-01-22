from pymongo import MongoClient

democlient = MongoClient()
myclient = MongoClient('localhost',27017)
mydb = myclient["demo"]      #db name
mycoll = mydb["dbtable"]     #collection name

mycoll.drop()                        #drop collection
democlient.drop_database("demo")     #drop db
print(myclient.list_database_names())