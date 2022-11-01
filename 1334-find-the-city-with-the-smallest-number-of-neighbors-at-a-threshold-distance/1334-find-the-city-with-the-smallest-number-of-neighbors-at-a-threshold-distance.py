class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = collections.defaultdict(list)
        k = distanceThreshold
        
        for u,v,w in edges:
            graph[u].append((v,w))
            graph[v].append((u,w))
        def numcities(node):
            heap = [(0,node)]
            visited = set()
            result = 0
            while heap:
                cost,cur_node = heapq.heappop(heap)
                if cur_node in visited:
                    continue
                if cur_node != node:
                    result += 1
                    
                visited.add(cur_node)
                
                for neighbour,new_cost in graph[cur_node]:
                    if cost+new_cost <= k:
                        heapq.heappush(heap,(cost+new_cost,neighbour))
            return result
        result = []
        
        
        for i in range(n):
            result.append(numcities(i))
        #print(result)
        return max([(numcities(city),city) for city in range(n)],key = lambda x:(-x[0],x[1]))[-1]   
                    