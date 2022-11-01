class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        row = len(grid)
        col = len(grid[0])
        res = []
        def dfs(i,j):
            if i >= row:
                res.append(j)
                return j
            if j >= col or j< 0 or i<0:
                return -1
            if grid[i][j] == 1 and (j+1 >= len(grid[0]) or grid[i][j+1]==-1):
                #print("hey2")
                return -1
            if grid[i][j] == -1 and (j-1 < 0 or grid[i][j-1] ==1):
                #print(i,j)
                #print("hey3")
                return -1
            if grid[i][j] == 1:
                return dfs(i+1,j+1)
            if grid[i][j] == -1:
                return dfs(i+1,j-1)
        result = []
        for i in range(1):
            for j in range(col):
                result.append(dfs(i,j))
        return result
                
        