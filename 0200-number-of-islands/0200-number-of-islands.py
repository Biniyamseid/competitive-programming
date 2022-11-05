from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def inrange(r,c):
            if r >= 0 and r <len(grid) and c >= 0 and c< len(grid[0]):
                return True
            return False
        visited = set()
        
        res = 0
        def bfs(r,c):
            q = deque()
            q.append((r,c))
            visited.add((r,c))
            while q:
                row,col = q.popleft()
                direction = [(0,1),(1,0),(0,-1),(-1,0)]
                for dr,dc in direction:
                    new_r,new_c = row+dr,col+dc
                    if inrange(new_r,new_c) and grid[new_r][new_c] == "1" and (new_r,new_c) not in visited:
                        q.append((new_r,new_c))
                        visited.add((new_r,new_c))
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r,c) not in visited and grid[r][c] == "1":
                    res += 1
                    bfs(r,c)
        return res
                    
                        
                   
        

                        