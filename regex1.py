from string import ascii_lowercase as lower
import re

x = 'abcaafabaabdfgz'

abc = ''

#for letter in lower:
#    abc += letter+'*'
#print(abc)

#abc = '*'.join(lower)
#abc += '*'
#print(abc)

abc = 'a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z*'

pat = re.compile(abc)

print(pat)
print(max(pat.findall(x),key=len))
