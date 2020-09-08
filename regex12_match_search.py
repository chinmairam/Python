# match() vs search()

import re

print(re.match('super', 'superstition').span())
print(re.match('super', 'insuperable'))

print(re.search('super', 'superstition').span())
print(re.search('super', 'insuperable').span())
