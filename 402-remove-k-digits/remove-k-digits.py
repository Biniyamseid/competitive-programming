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
        # num = [int(p) for p in num]
        # while k>=1:
            
        #     # if those are equal go and take the last one
        #     if num[0] == num[1]:
        #         j = 0
        #         while j<len(num)-1 and num[j]==num[j+1]:
        #             j+=1
        #         print(j)
        #         if num[j]>=num[j+1]:
        #             print(num[0:j],num[j+1:])
        #             num = num[0:j] + num[j+1:]
        #         else:
        #             print(num[0:j],num[j+1:])
        #             num = num[0:j+1] + num[j+2:]
        #     k-=1
        # num = [str(i) for i in num]
        # return "".join(num)
                
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
                # k-=1
            # elif c>stack[-1] and k<=1:
            #     k-=1
            # else:
            else:
                stack.append(c)
               
          
        while k>=1:
            stack = stack[0:-1]
            k-=1
        
        stack = [str(i) for i in stack]
        while stack[0] == "0" and len(stack)>1:
            stack = stack[1:]
        
        return "".join(stack)
            

        # take a stack if there comes minimum value pop the greate and insert the smaller

        # removed_indices = set()
        
        # i = 0
        # num = [int(i) for i in num]
        # print(num)
        # while k>=1:
        #     if len(num)>1:
        #         if num[0] == num[1]:
        #             j = 0
        #             while j<len(num)-2 and num[j]==num[j+1]:
        #                 j+=1
        #             print(j)
        #             if num[j]>=num[j+1]:
        #                 print(num[0:j],num[j+1:])
        #                 num = num[0:j] + num[j+1:]
        #             else:
        #                 print(num[0:j],num[j+1:])
        #                 num = num[0:j+1] + num[j+2:]

        #         elif num[0]>num[1]:
        #             removed_indices.add(0)
        #             num = num[1:]
        #         elif num[0]<=num[1]:
        #             removed_indices.add(1)
        #             num = [num[0]]+num[2:]
        #     k-=1
        # print(num)
        # while num[0]==0 and len(num)>1:
        #     num = num[1:]
        # num = [str(i) for i in num]
        # return "".join(num)

            
            
        

        