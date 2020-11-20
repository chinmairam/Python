s = 416729
x = str(s)
sum1 = sum2 = 0
for i in range(len(x)//2):
    sum1 += int(x[i])
for j in range(len(x)//2,len(x)):
    sum2 += int(x[j])
    

max_sum = max(sum1,sum2)
print(sum1, sum2)
print(max_sum)
