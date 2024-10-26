class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        visited= set()
        def dfs(r,c):
            if c<0 or c>=len(grid[0]) or r<0 or r>=len(grid) :
                return
            if (r,c) in visited:
                return
            if grid[r][c] != "1":
                return
            visited.add((r,c))
            
            for nr,nc in [(1,0),(0,-1),(0,1),(-1,0)]:
                dfs(r+nr,c+nc)
            return
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited and grid[i][j] == "1":
                    ans +=1
                    dfs(i,j)
        return ans
        
