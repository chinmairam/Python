L=[[2,3,5,1,8],[4,1,2,6,1],[6,4,5,7,9]]
mat = [[L[j][i] for j in range(len(L))] for i in range(len(L[0]))] 
print(mat)


s = "string is a string is a string"
print(set(s))
mydict = {k: s.count(k) for k in set(s)}
print(mydict)
