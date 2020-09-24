filename = 'copy.txt'

try:
    f = open(filename, 'r')
except OSError: # OSError replaces IOError from Python 3.3 onwards
    print("File could not be opened for read")
else:
    # Now we're sure the file is open
    print("Number of lines", sum(1 for line in f))
    f.close()
