from string import ascii_lowercase as lower

print(lower)

key = {}

for i in range(len(lower)):
    key[lower[i]] = i+1

print(key)

for k,v in key.items():
    print(k,v)
    

