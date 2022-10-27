class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges)+1)]
        def find(node):
            while node != par[node]:
                node = par[node]
            return node
        def union(x,y):
            par1 = find(x)
            par2 = find(y)
            par[par2] = par1
        for a,b in edges:
            if find(a) == find(b):return[a,b]
            union(a,b)
            
            