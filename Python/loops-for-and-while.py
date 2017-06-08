# note: Indentation is important because control flow is implied by indentation
# -------------------------------------------------------------------------------
fruit = ['apple', 'banana', 'pear', 'Grape', 'Orange']  # new array
new_fruit = []
for item in fruit:  # iterate
    print "The for-loop fruit item is " + item # prints each item isn array
    new_fruit.append(item)
print new_fruit # prints entire array
# -------------------------------------------------------------------------------
# Python: Dicts and Lists Together
sum = 0
numbers = [1, 2, 3, 5, 8]
for i in numbers:
    sum = sum + i
print i # i prints 8 only because while it loops through all, indentation only prints last
# -------------------------------------------------------------------------------
# Python: for Loops, with Lists
person = {'name': 'Philip Curtis', 'favorite_color': 'Black', 'hair': 'Brown'}
for key in person: # iterate
    print "key is " + key + ", value is " + person[key]
# Prints this:
# key is hair, value is Brown
# key is favorite_color, value is Black
# key is name, value is Philip Curtis
# -------------------------------------------------------------------------------
# Python: for Loops with Dicts
people = {'name': 'Bob', 'hometown': "Palo Alto", 'favorite_color': 'red'}
for item in people:
    if (item == 'favorite_color'):
        print people[item] # prints: red
# -------------------------------------------------------------------------------
# Python: while Loops
i = 0
while (i < len(fruit)): # len is a python operator telling length of a list, 3 here so 0,1,2
    print "The while-loop fruit is " + fruit[i]
    i = i + 1 # can not do i++ because not legal in python
