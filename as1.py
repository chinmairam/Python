def pal(n):
    temp=n
    rev=0
    while(n>0):
        dig=n%10
        rev=rev*10+dig
        n=n//10
    if(temp==rev):
        print("The number is a palindrome!")
    else:
        print("The number isn't a palindrome!")

def prime(num):
    if num > 1:  
   for i in range(2,num):  
       if (num % i) == 0:  
           print(num,"is not a prime number")  
           print(i,"times",num//i,"is",num)  
           break  
   else:  
       print(num,"is a prime number")  
         
else:  
   print(num,"is not a prime number")  

def even_or_odd(n):
    if n%2 == 0:
        print("even")
        return
    print("odd")

if __name__ == '__main__':
    pal(121)
    prime(10)
    even_or_odd(10)
