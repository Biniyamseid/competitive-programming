class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        @cache
        def helper(i1,i2):
            if i1 == len(a):
                return 0
            if i2 >= len(b):
                return float(-inf)
            take = a[i1]*b[i2] + helper(i1+1,i2+1)
            not_take = helper(i1,i2+1)
            return max(take,not_take)
        return helper(0,0)
        