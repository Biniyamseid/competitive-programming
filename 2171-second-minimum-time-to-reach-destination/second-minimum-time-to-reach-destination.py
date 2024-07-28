class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        
        D = [[] for _ in range(n + 1)]
        D[1] = [0]
        G, heap = defaultdict(list), [(0, 1)]
        
        for a, b in edges:
            G[a] += [b]
            G[b] += [a]

        while heap:
            min_dist, idx = heappop(heap)
            if idx == n and len(D[n]) == 2: return max(D[n])

            for neib in G[idx]:
                if (min_dist // change) % 2 == 0:
                    cand = min_dist + time
                else:
                    cand = ceil(min_dist/(2*change)) * (2*change) + time

                if not D[neib] or (len(D[neib]) == 1 and D[neib] != [cand]):
                    D[neib] += [cand]
                    heappush(heap, (cand, neib))
        