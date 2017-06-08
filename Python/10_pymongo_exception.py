# Program showing how exceptions work in Pymongo

#!/usr/bin/env python
import pymongo

# Do not need to import sys

connection = pymongo.MongoClient("mongodb://localhost")

db = connection.test # creates or connects to the database called 'test'
users = db.users # assign a variable called 'users' and create a collection called 'users'

doc = {'firstname':'FirstName-01', 'lastname':'LastName-01'} 
print doc
print "about to insert the document"

try:
    users.insert_one(doc)
except Exception as e:
    print "insert failed:", e

print doc
print "inserting again"
doc = {'firstname':'FirstName-02', 'lastname':'LastName-02'} # add this line to create another document with a seperate ID

try:
    users.insert_one(doc)
except Exception as e:
    print "second insert failed:", e # 'duplicate key error' caused because underscore_id must be unique within a collection.  Cannot have two documents with the same id.  This causes the failure.

print doc

