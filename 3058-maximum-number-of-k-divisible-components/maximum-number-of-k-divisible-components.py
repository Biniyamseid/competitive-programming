# class Solution:
#     def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
#         g = defaultdict(list)
#         for a,b in edges:
#             g[a].append(b)
#             g[b].append(a)
#         rolling_sum = 0
#         visited = set()
#         c = 0
#         cut = False
#         answers = set()
#         def dfs(node,count):
#             nonlocal rolling_sum
#             nonlocal cut
#             nonlocal c
#             if not g[node] or (node in visited):
#                 # if (not node  in visited) and node%k==0:
#                 #     c+=1
#                 return
#                 # if rolling_sum + values[node]%k == 0:
#                 #     return 
                   
#                 # else:
#                 #     return 0
#                 # return  count

#             if cut:
#                 rolling_sum = 0
            
   
#             rolling_sum+=values[node]
            
#             print("node",node)
#             print("rsum",rolling_sum)
#             visited.add(node)
#             if rolling_sum%k == 0: 
#                 answers.add(node)
#                 cut = True
#                 count +=1
#                 c+=1
#                 rolling_sum = 0
#                 return
#             else:cut = False

#             print("rsum2",rolling_sum)
#             for i in g[node][::-1]:
#                   dfs(i,count)

#             if   (node not in answers) and (not cut) and  (values[node]%k==0):
#                 if len(g[node])==1:
#                     c+=1
#                 elif not rolling_sum:
#                     c+=1
#                 # rolling_sum = 0
            
        
#         # ans = dfs(0,0)
#         ans = 0
#         for i in g:
#             if len(g[i])==1:
#                 dfs(i,0)
#         if not edges:
#             for i in values:
#                 if i%k==0:
#                     c+=1
#         for i in range(len(values)):
#             if i not in visited:
#                 dfs(i,0)


#         print(c)
#         print(visited,"visited")
#         return c
#         return ans
            
            
class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        ans = 0

        def dfs(node, parent):
            nonlocal ans

            # start with this node’s value mod k
            total = values[node]

            for nei in g[node]:
                if nei == parent:
                    continue
                child = dfs(nei, node)
                total = (total + child) % k

            # if entire subtree is divisible by k, it forms its own component
            if total % k == 0:
                ans += 1
                return 0

            return total

        dfs(0, -1)
        return ans
