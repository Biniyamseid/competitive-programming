from collections import defaultdict
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        manhattan = lambda x,y : abs(x[0]-y[0]) + abs(x[1]-y[1])
        n = len(points)
        graph = defaultdict(list)
        for i in range(n):
            for j in range(i+1,n):
                distance = manhattan(points[i],points[j])
                graph[i].append((distance,j))
                graph[j].append((distance,i))
        
        visited = set()
        minHeap = [(0,0)]
        result = 0
        while len(visited) < n:
            dist,node = heapq.heappop(minHeap)
            if node in visited:
                continue
            result += dist
            visited.add(node)
            
            for dn in graph[node]:
                if dn not in visited:
                    #result += d
                    heapq.heappush(minHeap,dn)
        return result
            
        
        