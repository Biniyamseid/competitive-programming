class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:
        ans = 0
        low= max(n-k,1)
        for i in range(low,n+k+1):
            if abs(n-i)<k or abs(n-i)==k:
                if n&i==0:
                    ans+=i
        return ans
        