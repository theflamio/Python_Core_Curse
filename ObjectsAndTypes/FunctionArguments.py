
#Function with default Argument Values
def banner(message, border='-'):
    line = border * len(message)
    print(line)
    print(message)
    print(line)

banner("Denmark is great")


banner("Denmark is great", ':-D')

#keyword argument border=
banner(message="Hello world", border='*')