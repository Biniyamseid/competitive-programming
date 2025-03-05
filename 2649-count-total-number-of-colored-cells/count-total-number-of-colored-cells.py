class Solution:
    def coloredCells(self, n: int) -> int:
        # return 1+(n-1)*4
        return 1+2*(n-1)*n
        ans = 1
        for i in range(1,n):
            ans+=i*4
        return ans

        