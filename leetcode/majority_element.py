"""
Write a function which takes an array and prints the majority element (if it exists),
  otherwise prints “No Majority Element”.
A majority element in an array A[] of size n is an element
  that appears more than n/2 times (and hence there is at most one such element).
"""
def findMajority(arr, n):
    maxCount = 0
    index = -1
    for i in range(n):
        count = 0
        for j in range(n):
            if(arr[i] == arr[j]):
                count += 1

        # update maxCount if count of
        # current element is greater
        if(count > maxCount):
            maxCount = count
            index = i
    # if maxCount is greater than n/2
    # return the corresponding element
    if (maxCount > n//2):
        print(arr[index])
 
    else:
        print("No Majority Element")

# Driver code
if __name__ == "__main__":
    arr = [1, 1, 2, 1, 3, 5, 1]
    n = len(arr)
 
    # Function calling
    findMajority(arr, n)
