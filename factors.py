n=int(input("Enter any no."))
print("Factors of ",n)
i=1
while i<=n:
    if n%i==0:
        print(i,end='\t')
    i=i+1
