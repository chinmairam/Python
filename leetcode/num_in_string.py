import re

text = "Prasad is 21 years old, Vijji is 12 years old."
result = re.split("\D+", text)
for i in result:
    print(i)
res = [i for i in result if i.strip()]
print(res)
print(max(res))
