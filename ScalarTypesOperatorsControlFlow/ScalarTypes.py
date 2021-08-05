##Intergers

# 0b10 -> binary

# 0o10 -> Octal

# 0x10 -> hex

# int(3.5) = 3  "cast to integer"


##floats float(7) -> 7.0

## None = null


## bool True False

# bool(0) = False any other is True

if True:
    print("It is True")

h = 42
if h > 50:
    print("Greater than 50")
else:
    print("Less than or equal to 50")

c = 5
while c != 0:
    print(c)
    c -= 1

## if remainder is 0 then the program stops

while True:
    response = input()
    if int(response) % 7 == 0:
        break

