"""
// Input: num = "1432219", k = 3
// Output: "1219"

1432219
1432219

if k is one
the best way is to remove the first or the second value
 so think like this every time remove the first or the second value while k>=1

 write a specific function that can solve 112 = 11
 
 if all are equal go and take the last one
"""

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k >= len(num):
            return "0"
        """
        "10200"
        [1]
        if k>=1: pop and add the check the zero thing
        [1] <- 0
        [0] <- 2
        [2] <- 0

        """
        stack = [0]
        for i in range(0,len(num)):
            c = int(num[i])
            if stack and  c<stack[-1]  and k>=1:
                while stack and k>=1 and c<stack[-1]:
                    stack.pop()
                    k-=1
                stack.append(c)
            else:
                stack.append(c)
               
          
        while k>=1:
            stack = stack[0:-1]
            k-=1
        
        stack = [str(i) for i in stack]
        while stack[0] == "0" and len(stack)>1:
            stack = stack[1:]
        
        return "".join(stack)
            

            
            
        

        