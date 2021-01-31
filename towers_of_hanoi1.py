def toh(src, dest, aux, n):
    if n==0:
        return
    print("Pre ",n)
    toh(src, aux, dest, n-1)
    print("At",n)
    toh(aux,dest,src,n-1)
    print("Post area in ",n)

toh("A","B","C",3)
