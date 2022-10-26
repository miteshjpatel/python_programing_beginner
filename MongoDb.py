# import MongoClient
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient['movie_db']
movies = myclient.movies

movie_ = {
    "Title":    "Mr.Robot",
    "Starting": "Rami Malek, Christian Slater, Carly Chaikin",
    "Created":  "Sam Esmail",
    "Year":     2016
}
# mycol = mydb["customer"]
id = movies.insert_one(movie_).inserted_id
print(id)
mydb.list_collection_names()

print(myclient.list_database_names())
