def is_even(x):
    return x % 2 == 0

print(callable(is_even))

is_odd = lambda x: x % 2 == 1
print(callable(is_odd))

print(callable(list))
print(callable(list.append))

class CallMe:
    def __call__(self):
        print("Called!")
my_call_me = CallMe()
print(callable(my_call_me))

print(callable("This is not callable"))
# String instances are not callable.

