##def bitStr(n, s):
##    if n == 1:
##        return s
##    return [digit + bits for digit in bitStr(1,s) for bits in bitStr(n-1,s)]
##
##print(bitStr(3,'abc'))

##from itertools import permutations 
##  
##def allPermutations(str): 
##       
##     # Get all permutations of string 'ABC' 
##     permList = permutations(str) 
##     #print(list(permList))
##     # print all permutations 
##     for perm in list(permList): 
##         print (''.join(perm)) 
##        
### Driver program 
##if __name__ == "__main__": 
##    str = 'ABC'
##    allPermutations(str) 

from itertools import permutations 
  
# Initialising string 
ini_str = "abc"
  
# Printing initial string 
print("Initial string", ini_str) 
  
# Finding all permuatation 
permutation = [''.join(p) for p in permutations(ini_str)] 
# Printing result 
print("Resultant List", str(permutation)) 
