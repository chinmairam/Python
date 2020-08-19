def first(iterable):
    iterator = iter(iterable)
    try:
        return next(iterator)
    except StopIteration:
        raise ValueError("iterable is empty")

print(first(["1st","2nd","3rd"]))
print(first({"1st","2nd","3rd"}))
print(first(set()))
