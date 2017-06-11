#!/usr/bin/env python
import pymongo
# Not necessary to import sys.  Sys is for exception handling
connection = pymongo.MongoClient("mongodb://localhost") # establish a connection to the database
db = connection.school # connect to school database
scores = db.scores # connect to scores collection

def find():

    print "find(), reporting for duty"

    query = {'type': 'exam'} # python dictionary query where type is exam

    try:
        cursor = scores.find(query) # will call find on above query returning a cursor, not a document as find_one, because multiple documents returned

    except Exception as e:
        print "Unexpected error:", type(e), e

    sanity = 0 # sanity limits the number of printed items to 10 & then breaking
    for doc in cursor: # iterate through documents returned in cursor
        print doc
        sanity += 1
        if (sanity > 10):
            break

def find_one():
    print "find_one(), reporting for duty"
    query = {'student_id': 10} # python dictionary query with a student id of 10
        # Note: Python dictionarys reuire the key to be in quotes

    # find_one put into a Try/Except block:
    try:
        doc = scores.find_one(query) # a find_one returns a document, not a cursor
            # Note: In Mongo shell it's findOne, in Python it's find_one
            # Note: Python is using new interface, the CRUD spec.
    except Exception as e:
        print "Unexpected error:", type(e), e
    print doc

if __name__ == '__main__':
    find()  # Change this to find_one() to run that function, instead.
    find_one()  
