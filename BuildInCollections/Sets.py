'''
Set

Unordered collection of unique elements.

Sets are mutable.

elements in a set must be immutable.

'''

p = {6, 34, 23, 556, 3434, 2323}

print(type(p))

d = {}
print(type(d))

t = [1, 4, 1, 1, 7, 4, 8]
print(t)
# set() removes dublicates
print(set(t))
print()

# adding and update
print(p)
p.add(345)
print(p)
p.update([36, 32, 324])
print(p)
print()

#remove objects "remove" cast an error i the object is not pressent but "discard" dose not
p.remove(32)
print(p)
print("32 has been removed and will not cast an error using discard")
p.discard(32)
print(p)

'''
Sets are commenly used in Set Algebra "mængde lærer"

union, difference and intersection or subset, superset and disjoint

'''

#examble

blue_eyes = {'Oliva', 'Harry', 'Lily', 'Jack', 'Amelia', 'Jones'}
blond_hair = {'Tom', 'Harry', 'Lily', 'Bradly', 'Amelia'}
smell_hcn = {'Tom', 'Harry'}
tast_ptc = {'Harry', 'Lily', 'Bradly'}
o_blood = {'Harry', 'Lily'}
b_blood = {'Jack', 'Jones'}
a_blood = {'Oliva', 'Amelia'}
ab_blood = {'Jones'}

# all people that have blue eyes or have blond hair
print(blue_eyes.union(blond_hair))

# all people that have blue eyes and blond hair
print(blue_eyes.intersection(blond_hair))

# all people with blond hair that do not have blue eyes
print(blond_hair.difference(blue_eyes))

# all people with blond hair and not blue eyes or blue eyes but not blond hair
print(blond_hair.symmetric_difference(blue_eyes))


