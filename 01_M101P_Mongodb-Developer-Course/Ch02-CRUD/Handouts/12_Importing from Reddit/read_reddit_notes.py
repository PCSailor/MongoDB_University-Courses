#!/usr/bin/env python
# This Python program reads data directly from Reddit and puts it in MongoDB
# Note: -m runs the module as a script

# First, must get a .json file from a reddit webpage
#   Bash Command:
        # cat reddit_notes.json | python -m json.tool | more
        # command that is a built in python system to deal with json
        # Cat a file, redirect to a Python module called 'json.tool', then send to 'more' and inspect the file

import json # enables parse the .json
import urllib2 # enables a web request to reddit.com
import pymongo
connection = pymongo.MongoClient("mongodb://localhost") # connect to mongo
db = connection.reddit # connect to the reddit database
stories = db.stories # use stories collection
stories.drop() # drop existing collection

url = "http://www.reddit.com/r/technology/.json"
hdr = { 'User-Agent' : 'phils mongo bot' }
req = urllib2.Request( url, headers=hdr )
reddit_page = urllib2.urlopen(req)

# reddit_page = urllib2.urlopen("http://www.reddit.com/r/technology/.json") 

# get the reddit home page using urllib2

parsed = json.loads(reddit_page.read()) # parse the json into python objects
for item in parsed['data']['children']: # iterate through every news item on the page # need data/children which is an array with each of the stories
    stories.insert_one(item['data']) # insert into mongo
