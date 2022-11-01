class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = collections.defaultdict(list)
        k = distanceThreshold
        
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
            
        def numcities(city):
            heap = [(0, city)]
            dist = {}
            result = 0
            
            while heap:
                cost,node = heapq.heappop(heap)
                if node in dist:
                    continue
                if node != city:
                    dist[node] = cost
                    result += 1
                for neigh,weight in graph[node]:
                    if neigh not in dist:
                        if weight+cost <= k:
                            heapq.heappush(heap,(weight+cost,neigh))
            return result
        
        return max([(numcities(city), city) for city in range(n)], key=lambda x: (-x[0], x[1]))[-1]
    