from math import factorial

s = {len(str(factorial(x))) for x in range(20)}
print(s)