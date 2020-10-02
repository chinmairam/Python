def trace(f, *args, **kwargs):
    print("args =", args)
    print("kwargs =", kwargs)
    result = f(*args, **kwargs)
    print("result =", result)
    return result

print(trace(int, "ff", base=16))
