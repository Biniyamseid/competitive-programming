class Solution:
    def isUgly(self, n: int) -> bool:
        dp = {}
        if not n:
            return False
        while n!=1:
            if n%2 == 0 : 
                n=n//2
            elif not n%3:
                n = n//3
            elif not n%5:
                n = n//5
            else:
                return False
        return True
                