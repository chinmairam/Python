# demo_reader/multi_reader.py

import os
from demo_reader.compressed import bzipped,gzipped

extension_map = {
    '.bz2': bzipped.opener,
    '.gz': gzipped.opener
    }

class MultiReader:

    def __init__(self, filename):
        #self.filename = filename
        #self.f = open(filename, 'rt')
        extension = os.path.splitext(filename)[1]
        opener = extension_map.get(extension, open)
        self.f = opener(filename, 'rt')

    def close(self):
        self.f.close()
    
    def read(self):
        return self.f.read()

# In REPL:
# import demo_reader.multi_reader
# r = demo_reader.multi_reader.MultiReader(
#                           'demo_reader/__init__.py')
# r.read()

# Create bz2,gz files using
# python -m demo_reader.compressed.bzipped test.bz2 data compressed with bz2
# python -m demo_reader.compressed.gzipped test.gz data compressed with gz
# Then,type in REPL:
#  from demo_reader.multi_reader import MultiReader
#  r = MultiReader('test.bz2')
#  r.read()
#  r = MultiReader('test.gz')
#  r.read()