class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        count = 0
        visited = set()
        def dfs(r,c):
            if r<0 or r>=n or c<0 or c>=m or (r,c) in visited or grid[r][c] =="0":
                return 
            visited.add((r,c))
            direction = [(1,0),(0,1),(-1,0),(0,-1)]
            for a,b in direction:
                nr,nc = r+a,c+b
                dfs(nr,nc)
        for i in range(n):
            for j in range(m):
                if (i,j) not in visited and grid[i][j] == "1":
                    count +=1
                    dfs(i,j)
        return count
                    