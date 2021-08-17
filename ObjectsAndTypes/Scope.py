# 4 types of scope

# local, Enclosing, Global, Buil-in "LEGB rule"

#exambel of bad use


count = 0
def show_count():
    print(count)

def set_count(c):
    count = c

show_count()
set_count(5)
show_count()

# To fix the issues of "shadow name from outer scope" use global keyword like below
def set_count_two(c):
    global count
    count = c

show_count()
set_count_two(5)
show_count()