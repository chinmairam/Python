def print_args(arg1, arg2, *args):
    print(arg1)
    print(arg2)
    print(args)

t = (11, 12, 13, 14)
print_args(*t)
