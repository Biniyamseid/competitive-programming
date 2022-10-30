class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m,n = len(grid),len(grid[0])
        direction = [(0,1),(1,0),(-1,0),(0,-1)]
        q = [(0,0,k)]
        step = 0
        seen = set()
        seen.add((0,0,k))
        while q:
            for _ in range(len(q)):
                r,c,k = q.pop(0)
                print(r,c,k)
                if r == m-1 and c == n-1:
                    return step
                for i in range(len(direction)):
                    nr,nc = direction[i][0] + r, direction[i][1] + c
                    if  nr < 0 or nr >= m or nc < 0 or nc >=n:
                        continue
                    newk = k - grid[nr][nc]
                    newstate = (nr,nc,newk)
                    if newk >= 0 and newstate not in seen:
                        q.append(newstate)
                        seen.add(newstate) 
            step += 1
        return -1
