class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if  not low%2  and not high%2:
            return (high-low)//2
        return (high-low)//2+1
        