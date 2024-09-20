# class Solution:
#     def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
#         cost = {}
#         weight = [float(inf) for i in range(len(flights))]
#         weight[src] = 0
#         for i,j,h in flights:
#             cost[(i,j)] =h
#         print(cost)
#         for i in range(k+1):
#             tempWeight = weight.copy()
#             print(i,"ahfdosssssssssss")
#             for c,(a,b) in enumerate(cost):
#                 print(a,b)
#                 tempWeight[b] = min(tempWeight[b],cost[(a,b)]+tempWeight[a])
#                 print(tempWeight)
#             weight = tempWeight
#         print(weight)
#         if weight[dst] == float(inf):
#             return -1
#         print(weight)
#         return weight[dst]

#         return 1
#         #first construct a graph
#         # graph = defaultdict(list)
#         # for i,j,h in flights:
#         #     graph[i].append([j,h])
#         # weight = [float(inf) for i in range(len(flights))]
#         # weight[0] = 0
#         # for a in range(k):
#         #     for i in range(n):
#         #         neighs = graph[i]
#         #         for j,h in neighs:
#         #             weight[i] = min(weight[i],)
#         #         # print(i,weight,graph)
#         #         # weight[i] = min(weight[i],weight[graph[i][0]]+graph[i][1])
#         # ans = weight[n-1]
#         # print(weight)
#         # if ans == float(inf):
#         #     return -1
#         # return ans
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float(inf) for j in range(n)]
        prices[src] = 0
        for i in range(k+1):
            curr = prices.copy()
            for s,d,p in flights:
                # if prices[s]==float(inf):
                #     continue
                if prices[s]+p <curr[d]:
                    curr[d] = prices[s]+p
            prices = curr
        print(prices)
        if prices[dst]==float(inf):prices[dst]=-1
        return prices[dst]

        