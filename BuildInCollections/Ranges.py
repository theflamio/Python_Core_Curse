'''

range(stop)

range(start, stop)

range(start, stop, step)

range dose not support keywords

'''

s = range(5)

for item in s:
    print(item)

print()
s = range(5, 10)

for item in s:
    print(item)

print()
s = range(0, 10, 2)

for item in s:
    print(item)

print('Tuble enumerate')
t = [6, 372, 8862, 148800, 2096886]
for items in enumerate(t):
    print(f'i = {items}')