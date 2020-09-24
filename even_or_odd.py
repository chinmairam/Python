def even_or_odd(n):
    if n%2 == 0:
        print("even")
        return
    print("odd")

w = even_or_odd(31)
print(w)
print(w is None)
