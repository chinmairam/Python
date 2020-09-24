for i in range(1,10):
    for j in range(10-i,1,-1):
        print(' ',end = '')
    for k in range(1,i+1):
        print(k,end = '')
    print()
