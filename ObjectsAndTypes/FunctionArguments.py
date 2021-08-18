
#Function with default Argument Values
def banner(message, border='-'):
    line = border * len(message)
    print(line)
    print(message)
    print(line)

banner("Denmark is great")


banner("Denmark is great", ':-D')

#keyword argument border=
banner(message="Hello world", border="*")

banner(border="*", message="Hello world")

# Remember that "def" is a statement executed at runtime

# Default arguments are evaluated when def is executed.

# Immutable default values don't cause problems "ALWAYS use immutable objects for default values"

def add_spam(menu=[]):
    menu.append('spam')
    return menu

print(add_spam(['Egg', 'beans']))
print(add_spam())
print(add_spam())

#Immutable Default Value

def add_spam_Two(menu=None):
    if menu is None:
        menu = []
    menu.append('spam')
    return menu

print(add_spam_Two())
print(add_spam_Two())
print(add_spam_Two())
