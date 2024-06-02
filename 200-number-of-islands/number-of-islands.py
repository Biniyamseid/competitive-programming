class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        visited = set()
        def dfs(r,c):
            if r<0 or r>=len(grid) or c<0 or c>=len(grid[0]):
                return
            if (r,c) in visited:
                return
            visited.add((r,c))
            neigh = [(1,0),(0,1),(-1,0),(0,-1)]
            for i,j in neigh:
                nextr = i+r
                nextc = j+c
                if nextr<0 or nextr>=len(grid) or nextc<0 or nextc>=len(grid[0]):
                    continue
                if (nextr,nextc) in visited or grid[nextr][nextc] != "1":
                    continue
                dfs(nextr,nextc)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in visited:
                    ans+=1
                  
                    dfs(i,j)
        return ans
        