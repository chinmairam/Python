def niven(n):
    sum1 = 0
    temp = n
    while temp > 0:
        sum1 += temp%10
        temp = temp // 10
    return n//sum1
print(niven(126))
