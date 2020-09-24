iterable = ['Spring','Summer','Autumn','Winter']
iterator = iter(iterable)
for i in range(len(iterable)):
    x = next(iterator) # next return each value one time
    print(x)
