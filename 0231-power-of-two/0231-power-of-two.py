class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n>0:
            return not (n & (n-1))
        
        return False