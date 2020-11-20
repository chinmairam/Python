x = [4,1,6,7,2,9]

sum1 = sum2 = 0
for i in range(len(x)//2):
    sum1 += x[i]
for j in range(len(x)//2,len(x)):
    sum2 += x[j]
    

max_sum = max(sum1,sum2)
print(sum1, sum2)
print(max_sum)
