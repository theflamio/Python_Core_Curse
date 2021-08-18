import datetime

'''
Strings functions
'''

s = 'New'
s += 'found'
s += 'land'

print(s)

#Strings are immutable. You can not modify them in place.

# use str.join() to join string instead of the + operator

# The + operator only results in temporaries

s = 'New'.join(['found', 'land'])
print(s)

# string Seperator
s = "unforgetable"
print(s.partition("forget"))

# "The age of {0} is {1}".format('Jim', 32)

# "Current position {latitude} {longitude}".format(latitude="60N", longitude="5E")

# PEP 489: Literal String Interpolation
value = 4 * 20
s = f"The value is {value}"
print(s)

print(f"The current time is {datetime.datetime.now().isoformat()}")