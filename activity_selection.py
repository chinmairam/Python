def printMaxActivities(s , f ): 
    n = len(f) 
    print("The following activities are selected")
  
    # The first activity is always selected 
    i = 0
    print(i) 
  
    # Consider rest of the activities 
    for j in range(n): 
  
        # If this activity has start time greater than 
        # or equal to the finish time of previously 
        # selected activity, then select it 
        if s[j] >= f[i]: 
            print(j) 
            i = j 
  
# Driver program to test above function 
# s = [1 , 3 , 0 , 5 , 8 , 5] 
# f = [2 , 4 , 6 , 7 , 9 , 9]
s = [1, 3, 2, 0, 5, 8, 11]
f = [3, 5, 4, 9, 7, 10, 12]
printMaxActivities(s , f) 
