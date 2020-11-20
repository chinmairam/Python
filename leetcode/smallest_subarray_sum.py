import math

def smallest_subarray_with_given_sum(s, arr):
    current_sum = 0
    min_length = math.inf
    start = 0

    for end in range(0, len(arr)):
        current_sum += arr[end] # add next element
        # shrink window as small as possible until the 'current_sum' is smaller
        #   than 's'
        while current_sum >= s:
            min_length = min(min_length, end-start+1)
            current_sum -= arr[start]
            start += 1
    if min_length == math.inf:
        return 0
    return min_length

def main():
    print("Smallest subarray length: "+str(smallest_subarray_with_given_sum(7, [2,1,5,2,3,2])))
    print("Smallest subarray length: "+str(smallest_subarray_with_given_sum(7, [2,1,5,2,8])))
    print("Smallest subarray length: "+str(smallest_subarray_with_given_sum(8, [3,4,1,1,6])))

main()
