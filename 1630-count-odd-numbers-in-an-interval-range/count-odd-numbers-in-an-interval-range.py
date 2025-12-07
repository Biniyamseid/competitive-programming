class Solution:
    def countOdds(self, low: int, high: int) -> int:
        
        return (high-low)//2 if  not low%2  and not high%2 else (high-low)//2+1
        
        