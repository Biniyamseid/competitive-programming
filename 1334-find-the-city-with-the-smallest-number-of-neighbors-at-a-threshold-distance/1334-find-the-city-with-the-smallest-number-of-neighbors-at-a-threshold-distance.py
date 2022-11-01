class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = collections.defaultdict(list)
        
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
            
        def getNumberOfNeighbors(city):
            heap = [(0, city)]
            dist = {}
            
            while heap:
                currW, u = heapq.heappop(heap)
                if u in dist:
                    continue
                if u != city:    
                    dist[u] = currW
                for v, w in graph[u]:
                    if v in dist:
                        continue
                    if currW + w <= distanceThreshold:
                        heapq.heappush(heap, (currW + w, v))
            return len(dist)
        
        return max([(getNumberOfNeighbors(city), city) for city in range(n)], key=lambda x: (-x[0], x[1]))[-1]