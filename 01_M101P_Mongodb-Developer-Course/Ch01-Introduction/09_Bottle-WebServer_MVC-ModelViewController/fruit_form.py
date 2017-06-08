import bottle

@bottle.route('/')
def home_page():
    mythings = ['apple', 'orange', 'banana', 'peach']
    # return bottle.template('hello_world', username='Andrew', things=mythings)
    return bottle.template('hello_world', {'username':"Richard", 'things':mythings})

@bottle.post('/favorite_fruit') # post handler taking a post request instead of get request
def favorite_fruit():
    fruit = bottle.request.forms.get("fruit") # gets the form element
    if (fruit == None or fruit == ""):
        fruit="No fruit selected"

    bottle.response.set_cookie("fruit", fruit) # sets a cookie to the value set by user
    bottle.redirect("/show_fruit") # redirect the browser to /show-fruit that sends a http response to browser telling it to redirect the browser and fetch (get request) another page

@bottle.route('/show_fruit') # get request
def show_fruit(): #f function called show_fruit
    fruit = bottle.request.get_cookie("fruit") # gets the cookie & returns fruit
    # from line 15 to line 20 involves a full response and new request from the browser

    return bottle.template('fruit_selection.tpl', {'fruit':fruit}) # returns the 'fruit_selection.tpl' template

bottle.debug(True)
bottle.run(host='localhost', port=7777)
