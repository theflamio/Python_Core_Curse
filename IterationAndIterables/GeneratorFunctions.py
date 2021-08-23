# Iterables defined by functions

# Lazy evaluation

# Can model sequences with no definite end

# Compsoable into pipelines

# Generators functions must include at least one yield statement

# They may also include return statements

def generator():
    yield 1
    yield 2
    yield 3

g = generator()
print(g) # type
print(next(g))
print(next(g))

#print(next(g)) calls a stop iteration
print()

for v in generator():
    print(v)

def generator2():
    print('Value 1')
    yield 1
    print('Value 2')
    yield 2
    print('Value 3')
    yield 3
    print('About to return')

for v in generator2():
    print(v)

print()
g = generator2()
print(g) # type
print(next(g))
print(next(g))