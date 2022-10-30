class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        if k >= m + n - 2: return m + n - 2  # if we can go by manhattan distance -> let's go
        
        DIR = [0, 1, 0, -1, 0]
        q = deque([(0, 0, k)])  # pair of (r, c)
        seen = set()
        seen.add((0, 0, k))
        step = 0
        while q:
            for _ in range(len(q)):
                r, c, k = q.popleft()
                if r == m - 1 and c == n - 1: return step  # Reach to the bottom right cell
                for i in range(4):
                    nr, nc = r + DIR[i], c + DIR[i + 1]
                    if nr < 0 or nr == m or nc < 0 or nc == n: continue  # Skip out of bound cells!
                    newK = k - grid[nr][nc]
                    newState = (nr, nc, newK)
                    if newK >= 0 and newState not in seen:
                        seen.add(newState)
                        q.append(newState)

            step += 1

        return -1