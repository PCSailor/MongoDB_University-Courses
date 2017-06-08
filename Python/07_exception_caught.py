import sys # must import sys

try: # try / except code control-block
    print 5 / 0 # indented code to try
except Exception as e: # exception e will catch almost all errors
    print "exception: ", type(e), e # print a caught exception with the type and the exception itself

print "but life goes on"

