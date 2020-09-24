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
    'nine': '9'}

def convert(s):
    """Convert a string to an integer"""

    # if not isinstance(s, list): # Checks whether argument is a list
    #    raise TypeError(
    #        "Argument must be a list")
    
    # x = -1
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        # x = int(number)
        return int(number)
        print(f"conversion succeeded! x = {x}")

    except (KeyError, TypeError) as e:
        # print("Conversion failed!")
        print(f"Conversion error: {e!r}",
              file=sys.stderr)
        raise
    #return x

def string_log(s):
    v = convert(s)
    return log(v)

# In Shell type:from exceptional import string_log
# string_log("two five".split()) 
# string_log("cat dog".split()) - Error
