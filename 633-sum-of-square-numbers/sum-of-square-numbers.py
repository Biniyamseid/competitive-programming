class Solution:
    def judgeSquareSum(self, c: int) -> bool:
            l = 0
            r = int(c**0.5) + 1  
        
            
            while l <= r:
                res = l**2 + r**2
                if res == c:
                    return True
                elif res < c:
                    l += 1
                else:
                    r -= 1
            
            return False
      



        