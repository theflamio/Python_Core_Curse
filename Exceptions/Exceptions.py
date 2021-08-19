'''

Exception concept

Raising exceptions

Control flow

Catching exceptions

Unhandled exceptions

Use in Python

Built in exceptions

Programmer vs user errors

Resource cleanup

'''
import sys
from math import log

DIGIT_MAP = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

def convert(s):
    ''' Convert a string into an integer from 0 to 9'''
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        return int(number)
    except (KeyError, TypeError)as e:
        # e"!r" will the include the information intro the string
        #print(f"Conversion error: {e}", file=sys.stderr)
        print(f"Conversion error: {e!r}", file=sys.stderr)
        raise #returns the error code to the caller

#print(convert('one zero zero'.split()))
#print()
#print(convert('around two grillion'.split()))
#print()
#print(convert(11))

def string_log(s):
    v = convert(s)
    return log(v)

print()
print(string_log('one zero zero'.split()))
print()
#print(string_log('around two grillion'.split()))
#print()
print(string_log(11))

'''

Exceptions are part of the API

'''

