from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db = client['book-library']
books_collection = db['books']