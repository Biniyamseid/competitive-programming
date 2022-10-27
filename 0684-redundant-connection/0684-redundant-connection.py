class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        par = [i for i in range(n+1)]
        print(par)
        
        def find(node):
            #print(node,"start")
            while par[node] != node:
                node = par[node]
                #print(node,"middle")
            #print(node)
            return node
        def union(n1,n2):
            
            p1 = find(n1)
            p2 = find(n2)
            if p1 != p2:
                par[p2] = p1
        for a,b in edges:
            #print(a,b)
           #print(par,'RTWH')
            if find(a) == find(b): return [a,b]
            union(a,b)
            #print(par,"after ")
            #print("    ")
            
            