from demo_reader.compressed.bzipped import opener as bz2_opener
from demo_reader.compressed.gzipped import opener as gzip_opener

__all__ = ['bz2_opener', 'gzip_opener']
#In REPL:
#from demo_reader.compressed import *
#from pprint import pprint
#pprint(locals())
#bz2_opener
#gzip_opener