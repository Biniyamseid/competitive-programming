class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==0:
            return False
        while n>1:
            n/=2
        if n==1:
            return True
        if n==0:
            return True
        return False
