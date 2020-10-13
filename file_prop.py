import os

def read_file(filename):
    if not os.path.exists(filename):
        return "1"
    if not os.path.isfile(filename):
        return "2"
    if not os.access(filename, os.R_OK):
        return "3"
    if is_locked(filename):
        return "4"
    if is_not_accessible(filenmae):
        return "5"

print(read_file("count.txt"))
print(read_file("copy.txt"))
