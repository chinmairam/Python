#print('executing multi-reader/__main__.py')
# Execute using:python multi-reader-program

import sys
from demo_reader.multi_reader import MultiReader

filename = sys.argv[1]
r = MultiReader(filename)
print(r.read())
r.close()

# python multi-reader-program test.bz2

# cd multi-reader-program
# python -m zipfile -c ../multi-reader-program.zip *
# cd ..
# dir multi-reader-program

# python multi-reader-program.zip test.bz2