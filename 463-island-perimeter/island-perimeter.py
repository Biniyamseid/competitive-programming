class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans = 0
        visited = set()
        def dfs(i,j):
            nonlocal ans
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or (i,j) in visited:
                return

            visited.add((i,j))

            
            
            dirn = [(0,1),(1,0),(-1,0),(0,-1)]
            for a,b in dirn:
                nr,nc = a+i,b+j
                if nr<0 or nr >=len(grid) or nc<0 or nc>=len(grid[0]):
                    ans +=1
                    
                elif grid[nr][nc] !=1:
                    ans+=1
                
                    



            for a,b in dirn:
                nr,nc = a+i,b+j
                if nr<0 or nr >=len(grid) or nc<0 or nc>=len(grid[0]):
                    continue
                if grid[nr][nc] == 1:
                    dfs(nr,nc)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    dfs(i,j)
        return ans

