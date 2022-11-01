class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        row = len(grid)
        col = len(grid[0])
        def dfs(i,j):
            if i >= row:
                return j
            if j >= col or j< 0 or i<0:
                return -1
            if grid[i][j] == 1 and (j+1 >= len(grid[0]) or grid[i][j+1]==-1):
                return -1
            if grid[i][j] == -1 and (j-1 < 0 or grid[i][j-1] ==1):
                return -1
            if grid[i][j] == 1:
                return dfs(i+1,j+1)
            if grid[i][j] == -1:
                return dfs(i+1,j-1)
        
        return [dfs(0,j) for j in range(col)]
                
        