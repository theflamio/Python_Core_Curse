import sys


def sqrt(x):
    '''
    Compute the square root using method of Heron of Alexandria

    Args:
        x: the number for which the square root is to be computed
    Returns:
        The square root of x.
    Raise:
        ValueError: If x is negative
    '''
    if x < 0:
        raise ValueError(f"Cannot compute square root of negative number {x}")
    guess = x
    i = 0
    while guess * guess != x and i < 20:
        guess = (guess + x / guess) /2.0
        i += 1
    return guess

def main():
    try:
        print(sqrt(9))
        print(sqrt(2))
        print(sqrt(-1))
    except ValueError as e:
        print(e, file=sys.stderr)

if __name__ == '__main__':
    main()