# Tubles

t = ("Denmark", 5.343, 34)

print(t)
print('t[0] =', t[0])
print('t[1] =', t[1])
print('t[2] =', t[2])
print('len(t) =', len(t))

print('Forloop items in a Tuble')
for item in t:
    print(item)

print()
print('To create a single element Tuble do as t = (343,)')
t = (343,)
print('Type Tuble')
print(type(t))
print('Type int')
t = (343)
print(type(t))

print()
print('Empty tuble = t = ()')
t = ()
print(type(t))

print()
print(' Unpacked tuble function')

def minmax(items):
    return min(items), max(items)

lower, upper = minmax([34,23,56,45,675,34,23,12])
print(lower)
print(upper)