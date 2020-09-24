x = 75
def myfunc():
    global x # without global x, UnboundLocalError
    x = x + 1
    print(x)

myfunc()
print(x)
