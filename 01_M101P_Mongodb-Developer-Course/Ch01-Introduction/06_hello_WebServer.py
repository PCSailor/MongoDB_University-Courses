import bottle
import pymongo
# handler for the default path of the web server
@bottle.route('/') # The GET request creating a default route
def index(): # decorator to run when user hits website
    connection = pymongo.MongoClient('localhost', 27017) # connect to mongoDB
    # db = connection.test # attach to test database
    db = connection.resume # attach to test database
    # name = db.names # get handle for names collection
    name = db.resume # get handle for names collection
    print "name = ", name
    item = name.find_one() # find a single document put in 'item' variable
    print "item = ", item
    return '<b>Hello %s!</b>' % item['name'] # returns 'Hello [whatever is in the 'name' key]
bottle.run(host='localhost', port=8082)
