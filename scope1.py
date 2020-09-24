# x = 20 # Global
def f1():
    # x = 20
    # global x
    x = 30
    def f2():
        nonlocal x # doesnot create new variable,overrides x
        x = 40 
        # x = 30 # Local
        print(x)
    f2()
    print(x)
x = 20 # Global
# f1()
# print(x)
