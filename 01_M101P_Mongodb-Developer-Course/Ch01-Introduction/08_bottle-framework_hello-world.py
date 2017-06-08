# Using the bottle framework
# building a web server
# Using Curl to view webpages within terminal

import bottle # import the framework bottle allowing access to the bottle methods

@bottle.route('/') # route decorator set to home website
def home_page(): # function with arbitury name 'home_page'
    # return "Hello World!\n" # function return
    return "<html><title</title><body>Hello World!\n</body></html>" # function return with correct HTML formating

@bottle.route('/testpage')
def test_page():
    return "<html><title</title><body>this is the test page\n</body></html>"

bottle.debug(True) # turns on debugging & like nodemon will not have to restart webserver everytime need to make a change
bottle.run(host='localhost', port=8090) # run command doing 2 things, 1) specifys the port (8080 is open to any user without needing admin priviledges) 2) gives the host name accepting request for as required by HTTP protocol so multiple web services can run on the same port

# Using Curl - Curl allows viewing these webpages within the terminal bash
# enter in terminal 'curl -i localhost:8090' & curl -i localhost:8090/testpage
# results (in terminal):
# HTTP/1.0 200 OK
# Date: Tue, 06 Jun 2017 11:20:13 GMT
# Server: WSGIServer/0.1 Python/2.7.13
# Content-Length: 62
# Content-Type: text/html; charset=UTF-8

# <html><title</title><body>this is the test page
# </body></html>