##def hypervolume(*lengths):
##    i = iter(lengths)
##    v = next(i)
##    for length in i:
##        v *= length
##    return v
##
##print(hypervolume(2,4)) # Rectangle
##print(hypervolume(2, 4, 6)) # Cube
##print(hypervolume(2, 4, 6, 8))
###print(hypervolume()) # StopIterationError

def hypervolume(length, *lengths):
    v = length
    for item in lengths:
        v *= item
    return v

print(hypervolume(3, 5, 7, 9))
print(hypervolume(3, 5, 7))
print(hypervolume(3, 5))
print(hypervolume(3))
print(hypervolume()) # TypeError
