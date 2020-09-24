def small(m,n): 
    x=[]
    for i in range(n):
        x.append(min(m))
        m.remove(min(m))
    print(x)

m = [14,15,10,12,19]
n = 2
small(m,n)

m = [811,152,405,107,103,200,960]
n = 3
small(m,n)


        
