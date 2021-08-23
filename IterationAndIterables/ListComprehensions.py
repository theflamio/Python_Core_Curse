
words = "Learning is something that you can do until the day you die. Not learning anything new is a bad day".split()

#constructs a new list were each length of the word is an element
print([len(word) for word in words])

#List Comprehension Syntax [expr(item) for item in iterable]

#Equivalent Syntax

lengths = []
for word in words:
    lengths.append(len(word))
print(lengths)