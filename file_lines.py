filename = 'copy.txt'

try:
    f = open(filename,'r')
except OSError:
    print("File could not be opened")
else:
    print("Number of lines", sum(1 for line in f))
    f.close()
