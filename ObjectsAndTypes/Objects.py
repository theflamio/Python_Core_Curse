#Python has named references to objects.

# Python creates an Int object with the value of 1000
x = 1000

# Python creates a new Int object with the value of 500. the old oject will be destroyed by the garbage collector
x = 500

# Experiment

a = 496
id(a)

b = 1729
id(b)

b = a
# Test of two object are the same
if id(a) == id(b):
    print('True')
    print(a)
# Test of two object are the same with the is operator
print(a is b)

# Augmented Assignment
t = 5
print(id(t), 'Object id')
t += 2
print(id(t), 'Changed Object id "object value 5 + object vaule 2 creates new object with value 7 then garbage collect two previous objects')

# Value Equality vs identity Equality
r = [4, 7, 11]

s = [4, 7, 11]

print('Check Identity Equality')

if id(r) == id(s):
    print('identity of r and s is equal = True')
else:
    print('identity of r and s is equal = False')

print('Check Value Equality')

if r == s:
    print('Value of r and s is equal = True')
else:
    print('Value of r and s is equal = False')

#Replacing Argument Value

f = [14, 23, 37]
print('Object f with the value =', f, 'Will NOT be replaced with [17, 28, 45]')
def replace(g):
    g = [17, 28, 45] # new list object has been made
    print('g =', g)

replace(f)

print(f, 'f Objects value was not changed since replace() made a new list object')

f = [14, 23, 37]
print('Object f with the value =', f, 'Will be replaced with [17, 28, 45]')
def replaceTwo(g):
    g.clear()
    g.append(17)
    g.append(28)
    g.append(45)
    print('g =', g)

replaceTwo(f)

print(f, 'f Object value is changed since replace() used object reference and cleared it then appended new values')