class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = []
        for i in range(rowIndex+1):
            dp.append([1]*(i+1))
        for i in range(rowIndex+1):
            for j in range(i):
                if j==0:
                    pass
                else:
                    dp[i][j] = dp[i-1][j-1]+dp[i-1][j]
        return dp[rowIndex]
        
        