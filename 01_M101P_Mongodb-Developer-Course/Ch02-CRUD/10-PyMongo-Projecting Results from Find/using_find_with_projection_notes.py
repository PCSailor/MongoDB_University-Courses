#!/usr/bin/env python
# Documentation for Mongo and PyMongo is very good to find out what something does inside PyMongo
    # Start with api.mongodb.org
        # api.mongodb.org
            [Mongodb-PyMongo-Python Documentation](http://api.mongodb.com/python/)
                # http://api.mongodb.com/python/2.7.1/
                    # API Documentation
                        # pymongo
                            # collection – Collection level operations
                                [find docs](http://api.mongodb.com/python/2.7.1/api/pymongo/collection.html#pymongo.collection.Collection.find)
# projection is similar to 'select' in a relational DB in that it lets one specifiy which fields you want back
# how to write a projection
#   first, call find,
#   Syntax: find {filter}, {projection}
#           find {filter-query to determine which documents to return}, { projection-which fields to return }
import pymongo
import sys

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the school database
db=connection.school
scores = db.scores


def find():

    print "find, reporting for duty"

    query = {'type': 'exam'} # python dictionary query to find the documents where the type is exam (Note: both type and exam are string literals)
    projection = {'student_id': 1, '_id': 0} # only return student_id field and suppress the _id field # 1 is include and 0 is exclude
#    projection = {'student_id': 1}

    try:
        cursor = scores.find(query, projection)

    except Exception as e:
        print "Unexpected error:", type(e), e

    sanity = 0  # sanity limits the number of printed items to 10 & then breaking
    for doc in cursor: # iterate through documents returned in cursor
        print doc
        sanity += 1
        if (sanity > 10):
            break


if __name__ == '__main__':
    find()
