class Solution:
    def maxJump(self, stones: List[int]) -> int:
        res = 0
        if len(stones) == 2:
            return stones[-1]
        for i in range(1, len(stones)-1):
            res = max(res, stones[i+1]-stones[i-1])
        return res
