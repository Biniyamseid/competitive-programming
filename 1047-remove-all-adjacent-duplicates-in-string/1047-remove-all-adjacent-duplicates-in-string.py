class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for i in s:
            if not stack:
                stack.append(i)
            else:
                if stack[-1] != i:
                    stack.append(i)
                else:
                    while stack and stack[-1] == i:
                        stack.pop()
                
        return "".join(stack)
            
                
        