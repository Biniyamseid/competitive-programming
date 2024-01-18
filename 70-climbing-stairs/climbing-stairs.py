class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def dp(q):
            if q>=n:
                return 1
            step1= 0+dp(q+1)
            step2 = 0+dp(q+2)
            return step1+step2
        return dp(1)            
        