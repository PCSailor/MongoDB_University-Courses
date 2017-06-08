# Pymongo is the glue connecting a program to the database // like Mongoose in Node
import pymongo
from pymongo import MongoClient  # from Pymongo importing MongoClient
connection = MongoClient('localhost', 27017)# connection = MongoClient('localhost', 27017)  # connect to database
# db = connection.test  # test database
# names = db.names  # variable created as connection to names collection
# item = names.find_one()  # variable created to find one field within the names collection
# print item['name']
db = connection.resume
names = db.resume
item = names.find_one()
print item['name']
