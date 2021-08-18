'''

Index from the end of sequences using negative numbers.

The last element is at index -1

'''

r = [1, -4, 10, -16, 15]
print(r[-1])
print(r[-2])
# clunky way
print()
print(r[len(r) - 1])

'''

Slicing 

Extended form of indexing for referring to a porting of a list or other sequence.

Syntax: a_list[start:stop]

'''

r = [1, -4, 10, -16, 15]
print('Slicing from index 1 to 3')
print(r[1:3])
print('Slicing from index 2 to the end')
print(r[2:])
print('Slicing from index 3 to the start')
print(r[:3])

#copy of a list
s = r[:]
print(s is r)
print(s == r)
# copy is prettier
s = r.copy()
print(s is r)
print(s == r)

print()

w = "the dum from school always thinks they are smart but when reallity hits them and finally realise it is to late for them".split()
#i = w.index('unicorn')
#print(i)
i = w.count('them')
print(i)

print()
print('them' in w)
print('them' not in w)
# del w[2]
w.remove('them')
print(w)

print()
m = [2, 1, 3]
n = [4, 7, 11]
k = m + n
print(k)
k += [18, 29, 47]
print(k)
k.extend([76, 129, 199])
print(k)

print()
# reverse() and sort()
k.sort(reverse=True)
print(k)
