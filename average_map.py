n, x = map(int,input().split())
arr = [0 for i in range(n)]
for i in range(x):
    temp_arr=list(map(float,input().split()))
    for j in range(n):
        arr[j] += temp_arr[j]
print(arr)
for i in range(n):
    print(arr[i]/x)

# Input like this
##5 3 # 5-No.of students,3-No.of subjects
##89 90 78 93 80
##90 91 85 88 86
##91 92 83 89 90.5
