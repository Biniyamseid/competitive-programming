class Solution:
    def shortestPath(self,grid,k):
        m,n = len(grid),len(grid[0])
        direct = [(0,1),(1,0),(0,-1),(-1,0)]
        q = ([(0,0,k)])
        seen = set()
        seen.add((0,0,k))
        step = 0
        while q:
            for _ in range(len(q)):
                r,c,k = q.pop(0)
                if r >= m-1 and c >= n-1:
                    return step
                for i in range(4):
                    nr = direct[i][0]+r
                    nc = direct[i][1]+c
                    if nr < 0 or nr >= m or nc < 0 or nc>= n:
                        continue
                    newk = k -  grid[nr][nc]
                    newstate = (nr,nc,newk)
                    if newk >= 0 and newstate not in seen:
                        seen.add(newstate)
                        q.append(newstate)
            step += 1
        return -1
