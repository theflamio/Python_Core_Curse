from urllib.request import urlopen

# String
# 'Flemming' or "Flemming" important is that you are consistance about it
#

# for newlines Multiline string and Escape sequences like \n
""" this is
a multiline
string"""

'''So 
is 
this.'''

# r prefix is to supress escape mechanisme
path = r'C:\Users\FLEMMING.CHRISTENSE'
print(path)

s = 'parrot'
print(s[4])

#type(s[4]) shows it is class 'str' in the python virtual enviroment

# in python consol help(str) shows you all the functions string class have

c = 'oslo'
print(c)
# returns a new string called Oslo
c = c.capitalize()
print(c)

## bytes are prefixed with b

''' Data type for sequences of bytes, Raw binary data, Fixed-width single-byte encodings'''

# b'data'

## list "array"

''' Sequences of object Mutable"can be changed" A workhorse in Python'''

a = [1, 5, 7]

print(a)
a.append(34)
print(a)
print(a[0])

## dict "dictonary" "Maps"
'''Fundamental data structure in Python, Map keys to values, Also known as maps or associative arrays '''

d = {'Alice': '75775418', 'Bob': '75773829'}

print(d['Alice'])
d['Alice'] = '75775420'
print(d['Alice'])

# Asign a key that do not exist in the dict will creat a new key
d['Eve'] = '75776425'
print(d)

## for-loop
for item in d:
    print(item, d[item])

## putting it all togetter

story = urlopen('http://sixty-north.com/c/t.txt')

story_words = []

for line in story:
    line_words = line.split()
    for word in line_words:
        story_words.append(word)

# remember to close after use :)
story.close()
print("Bytes b'something'")
print(story_words)

story_words.clear()

story = urlopen('http://sixty-north.com/c/t.txt')

for line in story:
    line_words = line.decode('utf8').split()
    for word in line_words:
        story_words.append(word)

story.close()
print('without bytes indectation')
print(story_words)