# Copied from '04_hello_bottle__m101p_54ffa9bcd8ca390acc94ceef.py'
# www.bottlepy.org
# cmd: pip install bottle

from bottle import route, run, template # imports methods: route, run, and template

@route('/hello/<name>') # using decorators to set up URLs that web server will listen for 
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name) # here will return a template URL with /hello/<name> where name is a variable

run(host='localhost', port=8085) # Here it is listening on URL localhost:8085

