# Python default reads files in 'utf-8'

# all open() Modes have
#                       r = open for reading
#                       w = open for writing
#                       a = open for appending
#
# and Selector
#                       b = binary mode
#                       t = text mode

# this example open for writing in text mode.
f = open('wasteland.txt', mode='wt', encoding='utf-8')
f.write("Hello World")
f.close()

# open for reading int text mode.
g = open('wasteland.txt', mode='rt', encoding='utf-8')
print(g.readline())
