"""You are given a bag with n balls.Each ball has a value v[i] assigned to it.
You have to pick 5 balls from the bag such that their profit is maximized"""
#Approach:
# 1.Get 5 max positive values, 5 max negative values.
# 2.Try all possible combinations of these.1.via bit manipulation.
# 3.Choose the maximum one.

# 0000011111 = 31
# ...
# 1111111111 = 2^10 - 1

def get_set_bits(num):
    #return [0,1,2,3,4] # For 31:setbits at places 0,1,2,3,4;(16+8+4+2+1=31)
    set_bits = []
    for i in range(0,32):
        if (1<<i & num) > 0:
            set_bits.append(i)
    return set_bits

'''
3
00000101
       1 = When 'and' return value > 0
      10 = value = 0
     100 = value > 1
'''

n = int(input("Enter no.of balls: "))
arr = list(map(int, input("Enter values: ").split()))

pos_values = []
neg_values = []

arr.sort()
# sorted array[-ves,0,+ves]

i = 0
while i < 5 and arr[i] < 0:
    neg_values.append(arr[i])
    i = i + 1

i = 0
while i < 5 and arr[-1-i] >= 0:
    pos_values.append(arr[-1-i])
    i = i + 1

shortlisted = neg_values + pos_values
print(f"shortlisted array is {shortlisted}")

# You can also use itertools to do the below method.
ans = (shortlisted[0])**5 # smallest negative value.
# ans = (-3000)**5

for i in range(31, 2**len(shortlisted)):
    set_bits = get_set_bits(i)
    #print(set_bits)
    if len(set_bits) == 5:
        product = 1
        for j in set_bits:
            product = product * shortlisted[j]
        ans = max(ans, product)

print(ans)

#Enter no.of balls: 11
#Enter values: 5 4 6 -3 -5 1 10 8 7 -2 9
#shortlisted array is [-5, -3, -2, 10, 9, 8, 7, 6]
#30240
    
