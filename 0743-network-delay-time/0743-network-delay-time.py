class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for src,dst,c in times:
            graph[src].append((dst,c))
        queue = [(0,k)] #(cost,node)
        visited = set()
        max_cost = 0
        
        while queue:
            #always pop the minimum value
            cost,node = heapq.heappop(queue)
            if node in visited:
                continue
            visited.add(node)
            max_cost = max(max_cost,cost)
            neighbours = graph[node]
            for neighbour in neighbours:
                new_node,new_cost = neighbour
                if new_node not in visited:
                    curr_cost = cost + new_cost
                    heapq.heappush(queue,(curr_cost,new_node))
        return max_cost if len(visited) == n else -1
        