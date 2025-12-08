import math
class Solution:
    def countTriples(self, n: int) -> int:
        ans = 0
        for i in range(1,n+1):
            for j in range(i+1,n+1):
                if  int(math.sqrt(i**2+j**2))<=n and  i!=j!= math.sqrt(i**2+j**2) and math.sqrt(i**2+j**2) ==int(math.sqrt(i**2+j**2)):
                
                    ans +=2

        return ans

        