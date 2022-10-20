# import MongoClient

from pymongo import MongoClient

#Creating a Client
client = MongoClient('localhost', 27017)

#Creating a database name mongodb
db = client['mydb']

list_of_db = client.list_database_names()
if "mydb" in list_of_db:
    print("DB EXISTS !!!")
