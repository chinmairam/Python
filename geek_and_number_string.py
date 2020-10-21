class Solution:
    def minLength(self, s, n): 
        st = []
        list1 = ["12", "21", "34", "43", "56", "65", "78", "87", "09", "90"]

        for i in range(n): 
            if len(st) == 0:
                st.append(s[i])
            else:
                temp = ""
                temp += st[-1]
                temp += s[i]

                flag = 0
                for j in range(len(list1)):
                    if list1[j] == temp:
                        flag = 1

                if flag==1:
                    st.pop()
                else:
                    st.append(s[i])
        return len(st) 

if __name__ == '__main__':
    t = int(input("Enter no.of inputs:"))
    for _ in range(t):
        n = int(input("Enter size of array:"))
        s = input("Enter the string:")
        ob = Solution()
        print(ob.minLength(s, n))

# Give input as:
#Enter no.of inputs:1
#Enter size of array:5
#Enter the string:12213
"""
Output: 1
Explanation:
Geek can get the string of 
length 1 in two minimising operation,
In 1st operation Geek will remove "12" 
from "12213" then Geek left with "213"
In 2nd operation Geek will remove "21" 
from "213" then Geek left with "3"
"""
