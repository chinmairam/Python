def fact(n):
    if n==0:
            return 1
    else :
            return n*fact(n-1)


x = fact(44)    # x =2658271574788448768043625811014615890319638528000000000L
y=str(x)[::-1] # convert x to string and inverse it
print(y)
print(str(int(y))[0])  # convert y to int after to string and get the first char 


#8
# int(y) removes leading zeroes
#  Ex:str(120)[::-1] = '021'
#     int(str(120)[::-1]) = 21
