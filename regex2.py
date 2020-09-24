import re

dad = 'dadaddadaadada'

found = re.findall(r'(?=(\w\w\w))',dad)

#(?=...)  Matches if ... matches next, but doesn't consume the string.

#found = re.findall(r'(?=(\w+))',dad)

dads = [dad for dad in found if dad == 'dad']

print(len(dads))
