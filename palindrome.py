def pal(x):
    if x == x[::-1]:
        return True
    else:
        return False

print(pal("Bob"))
print(pal("Sam"))
print(pal("bob"))
