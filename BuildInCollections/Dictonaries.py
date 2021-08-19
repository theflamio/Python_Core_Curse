# Dictornaries

#example of a dict "keys: values"
'''
Key objects must be immutable and uniq

Value objects are mutable

tubles can be converted to dict via the dict keyword "dict"
'''

urls = { 'Google': 'http://google.com',
         'Pluralsight': 'http://pluralsight.com',
         'Sixty North': 'http://sixty-north.com',
         'Microsoft': 'http://microsoft.com'}

print(urls['Pluralsight'])
print()
# copy of dict is as the same with list you do not copy the object only the values

e = urls.copy()
print(urls is e)
print(urls == e)
print()

# if the key is already in the dict only the value is updated
print(urls)
urls.update({'Sixty North': 'http://Sixty-North.com'})
print(urls)
print()

# prints out key and value
for key in urls:
    print(f"{key} => {urls[key]}")

# prints out keys
for key in urls.keys():
    print(key)

# prints out values
for value in urls.values():
    print(value)

# prints out key and value
for item in urls.items():
    print(item)