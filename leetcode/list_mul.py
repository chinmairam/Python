n=int(input("Enter no.of test cases:"))
product = 1
for i in range(n):
    arr = input().split()
    for num in arr:
        product *= int(num)
    print(product)


    
