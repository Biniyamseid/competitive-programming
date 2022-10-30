class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.count = n
        #self.rank = [1 for _ in range(n)]
    
    # make a and b part of the same component
    # union by rank optimization
    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)
        if pa == pb: return False
        self.parent[pb] = pa
        self.count -= 1
        return True
        
    
    # find the representative of the 
    # path compression optimization
    def find(self, a):
        while self.parent[a] != a:
            a = self.parent[a]
        return a

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        manhattan = lambda x,y:abs(x[0]-y[0])+abs(x[1]-y[1])
        
        n = len(points)
        edges = []
        for i in range(n):
            for j in range(i+1, n):
                dist = manhattan(points[i],points[j])
                edges.append((dist, i, j))
        heapq.heapify(edges)
        ds = DisjointSet(n)
        res = 0       
        while edges and ds.count>1:
            cost,u,v = heapq.heappop(edges)
            if ds.union(u,v):
                res += cost
        return res