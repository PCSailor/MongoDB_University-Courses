# Defining a function inside Python
fruit = ['apple', 'orange', 'grape', 'kiwi', 'orange', 'apple'] 
def analyze_list(l): # reports list item frequency
    counts = {} # creation of Python Dicts (dictionary like object)
    for item in l:
        if item in counts: # see below
            counts[item] = counts[item] + 1
        else: # see below
            counts[item] = 1 # see below
    return counts

counts = analyze_list(fruit) # analyze a list
print counts
# Note: Without these three lines: 
        #     if item in counts:
        #         else:
        #     counts[item] = 1
        # you can not access items from a dictionary prior to setting it.
        # When Python finds the first apple and then trys to set 'count of apple' equal to 'count of apple + 1' it is trying to dereference something that is undefined.
        # The If/Else checks to see if it is in there