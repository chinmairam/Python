import sys

def sqrt(x):
    """Compute square roots using the method
    of Heron of Alexandria"""

    if x < 0:
        raise ValueError(
            "Cannot compute square root of "
            f"negative number {x}")
    
    guess = x
    i = 0
    while guess * guess != x and i < 20:
        guess = (guess + x / guess) / 2.0
        i += 1
    return guess

def main():
    try:
        print(sqrt(9))
        print(sqrt(2))
        print(sqrt(-1))
        print("This is never printed.")
    #try:
    #    print(sqrt(-1))
    # except ZeroDivisionError:
    #   print("Cannot compute square root of a negative number.")
    except ValueError as e:
        print(e, file=sys.stderr)

    print("Program execution continues "
          "normally here.")

if __name__ == '__main__':
    main()
