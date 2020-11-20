import sys
 
def solution(A):
    #1st pass
    parts = [0] * len(A)
    parts[0] = A[0]
  
    for idx in range(1, len(A)):
        parts[idx] = A[idx] + parts[idx-1]
  
    #2nd pass
    solution = sys.maxsize
    for idx in range(0, len(parts)-1):
        solution = min(solution,abs(parts[-1] - 2 * parts[idx]));  
  
    return solution

x=1,2,3,4,5
print(solution(x))
