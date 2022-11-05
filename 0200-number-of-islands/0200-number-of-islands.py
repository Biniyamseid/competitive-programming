from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def inrange(r,c):
            if r>=0 and r < len(grid) and c>=0 and c<len(grid[0]):
                return True
            return False
        rows,cols = len(grid),len(grid[0])
        visited = set()
        
        res = 0
        def bfs(r,c):
            q = deque()
            q.append((r,c))
            visited.add((r,c))
            while q:
                row,col = q.popleft()
                directions = [(1,0),(-1,0),(0,1),(0,-1)]
                for dr,dc in directions:
                    newr,newc = row+dr,col+dc
                    if inrange(newr,newc) and grid[newr][newc] == "1" and (newr,newc) not in visited:
                        q.append((newr,newc))
                        visited.add((newr,newc))
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and  grid[r][c] == "1":
                    bfs(r,c)
                    res += 1
        return res
                        
                   
        

                        