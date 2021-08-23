iterable = ['Spring', 'Summer', 'Autumn', 'Winter']

iterator = iter(iterable)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
#print(next(iterator))

def first(iterable):
    iterator = iter(iterable)
    try:
        return next(iterator)
    except StopIteration:
        raise ValueError("iteralbe is empty")

first(['1','2','3'])
first([])

