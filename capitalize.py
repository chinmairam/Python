import sys

for line in sys.stdin:
    print(line.strip().capitalize())


# run:type haiku.txt | python capitalize.py
#          or
# run:python capitalize.py < haiku.txt
#         |  = pipe.
#         <  = redirection operator in command line shell.
