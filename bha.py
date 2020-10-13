
def count(x, y):
    try:
        return None
    except:
        return x+y
    finally:
        return x**y

a = 5
b = 4
c = count(a,b)
print(c)
