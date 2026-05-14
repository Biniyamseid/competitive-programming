import heapq
class Solution:
    def minCost(self, n: int, prices: List[int], roads: List[List[int]]) -> List[int]:
            # adj1 for empty travel, adj2 for loaded travel
            adj1 = [[] for _ in range(n)]
            adj2 = [[] for _ in range(n)]
            for u, v, cost, tax in roads:
                adj1[u].append((v, cost))
                adj1[v].append((u, cost))
                adj2[u].append((v, cost * tax))
                adj2[v].append((u, cost * tax))

            def dijkstra(start_node, adj):
                dist = [float('inf')] * n
                dist[start_node] = 0
                pq = [(0, start_node)]
                while pq:
                    d, u = heapq.heappop(pq)
                    if d > dist[u]: continue
                    for v, weight in adj[u]:
                        if dist[v] > d + weight:
                            dist[v] = d + weight
                            heapq.heappush(pq, (dist[v], v))
                return dist

            # Precompute all-pairs shortest paths
            # d1[i][j] is min cost to go from i to j empty
            # d2[i][j] is min cost to go from i to j loaded
            d1 = [dijkstra(i, adj1) for i in range(n)]
            d2 = [dijkstra(i, adj2) for i in range(n)]

            ans = []
            for i in range(n):
                res = prices[i] # Option: Buy locally
                for j in range(n):
                    # Option: Go to j empty, buy, come back loaded
                    current_trip = d1[i][j] + prices[j] + d2[j][i]
                    res = min(res, current_trip)
                ans.append(res)
            
            return ans
        

        