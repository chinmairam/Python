def pal(x):
    if x == x[::-1]:
        return True
    else:
        return False

print(pal('121'))
print(pal('345'))
print(pal('545'))
