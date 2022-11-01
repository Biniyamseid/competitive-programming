class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))
        visited = set()
        heap = [(0,k)] # (cost,node)
        max_cost = 0
        while heap:
            cost,node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            max_cost = max(max_cost,cost)
            neighbours = graph[node]
            for neighbour in neighbours:
                new_node,new_cost = neighbour
                if new_node not in visited:
                    heapq.heappush(heap,(cost+new_cost,new_node))
        return max_cost if len(visited) == n else -1
            
        