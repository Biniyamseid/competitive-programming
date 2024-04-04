class Solution:
    def maxDepth(self, s: str) -> int:
        # check if it is valid parentheses
        ans = 0
        deep = 0
        for i in s:
            if i=="(":
                deep+=1
            elif i==")":
                deep-=1
            ans = max(deep,ans)
        return ans
            
        