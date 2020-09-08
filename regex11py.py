import re

s = '<html><head><title>Title</title>'
print(len(s))
print(re.match('<.*>', s).span())
print(re.match('<.*>', s).group()) #Greedy
print(re.match('<.*?>', s).group()) #Non-Greedy
