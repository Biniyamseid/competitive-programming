from collections import defaultdict
class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        # from 1 to c one based indexing, 
        # build connections
        grids = defaultdict(list)
        for u,v in connections:
            grids[u].append(v)
            grids[v].append(u)
        online = set()
        station_group = dict()
        minheaps = defaultdict(list)
        visited = set()

        def dfs(station,id):
            if station in visited:
                return
            visited.add(station)
            online.add(station)
            station_group[station]= id
            heappush(minheaps[id],station)
            for stat in grids[station]:
                dfs(stat,id)
        result = []
        
        for i in range(1,c+1):
            dfs(i,i)
            
        for j,x in queries:
            
            if j == 1:
                if x in online:
                    result.append(x)
                else:
                    groupid = station_group[x]
                    min_heap = minheaps[groupid]
                    while min_heap and not (min_heap[0]  in online):
                        heappop(min_heap)
                    if min_heap:
                        result.append(min_heap[0])
                    else:
                        result.append(-1)
            else:
                online.discard(x)

        return result
                    
            
            






#         def dfs(k,visited,found):
#             if len(d[k])==0 or found or k in visited:
#                 return []
            
#             visited.add(k)
#             result = []
#             if not (k in offline):
#                 result.append(k)
#             for i in d[k]:
#                 result.extend(dfs(i,visited,found))
#             return result
#         d = defaultdict(set)
#         offline = set()
#         answer = []
#         grid = set()
#         for i,c in connections:
#             grid.add(i)
#             grid.add(c)
#             d[i].add(c)
#             d[c].add(i)
#         grid = sorted(list(grid))
#         grid_set = set(grid)
        
#         for l,r in queries:
#             if l ==1:
#                 if r not in offline:
#                     answer.append(r)
#                 else:
#                     found = 0
#                     reachable_online = dfs(r,set(),0)
#                     if  not reachable_online :
#                         answer.append(-1)
#                     else:
#                         answer.append(min(reachable_online))
#             if l ==2:
#                 offline.add(r)
#         return answer



        