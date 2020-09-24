arr = list(map(int,input().split()))
arr = sorted(arr)
print(arr)
if arr[0] <= 0:
    print("False")
else:
    flag = False
    for i in arr:
        s = str(i)
        if s==s[::-1]:
            flag = True
            break
    print(flag)
