# See 08_bottle-framework_hello-world.py for basic code-file notes
# refer to the mvc.png
# With the MVC, it is wiser code to seperate the controller from the user-views
# When using templates, a folder called 'views' must be used
import bottle

@bottle.route('/') # route decorator
def home_page(): # this is the controller
    mythings = ['apple', 'orange', 'banana', 'peach'] # array list
    # the user-view is seperated from the controller by using a view-template with the extension .tpl
    # return bottle.template('hello_world', username='named parameter', things=mythings) # template called with named parameters
    return bottle.template('hello_world', {'username':"dictionary", 'things':mythings}) # template called using a dictionary

@bottle.post('/favorite_fruit')
def favorite_fruit():
    fruit = bottle.request.forms.get("fruit")
    if (fruit == None or fruit == ""):
        fruit="No fruit selected"

    return bottle.template('fruit_selection.tpl', {'fruit': fruit})


bottle.debug(True)
bottle.run(host='localhost', port=7777)
