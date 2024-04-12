class Solution:
    def trap(self, height: List[int]) -> int:
        """ 0 
        1 2 = 1
        2 - 1 - 0 1 3 = 2
        3 - 2 1 2  1
        """
        n = len(height)
        ans = 0
        maxLeft,maxRight = [0]*n,[0]*n
        for i in range(1,n):
            maxLeft[i] = max(height[i-1],maxLeft[i-1])
        for i in range(n-2,-1,-1):
            maxRight[i] = max(height[i+1],maxRight[i+1])
        
        for i in range(n):
            waterlevel = min(maxLeft[i],maxRight[i])
            if waterlevel >= height[i]:
                ans += waterlevel - height[i]
        return ans
        