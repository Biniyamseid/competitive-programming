class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        r,c=len(grid),len(grid[0])
        dp = [[0 for i in range(c+2)] for j in range(r+2)]
        for i in range(r):
            for j in range(c):
                if j==0:
                    
                    dp[i+1][j+1] = dp[i][j+1]+grid[i][j]

                elif i == 0:
                    
                    dp[i+1][j+1] = dp[i+1][j]+grid[i][j]
                    
                else:
                    dp[i+1][j+1] = min(dp[i][j+1],dp[i+1][j])+grid[i][j]
        
        return dp[r][c]
    
        