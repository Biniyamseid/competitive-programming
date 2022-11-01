class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n,m = len(heights),len(heights[0])
        target = (n-1,m-1)
        heap = [(0,(0,0))]
        dist = {(0,0):0}
        abs_dif = lambda x,y:abs()
        while heap:
            cost,node = heapq.heappop(heap)
            x,y = node
            if node == target:
                break
            for i,j in [(0,1),(0,-1),(-1,0),(1,0)]:
                newx,newy = x+i,y+j
                if newx >=0 and newx<n and newy<m and newy >=0:
                    newedge = max(cost,abs(heights[newx][newy] - heights[x][y]))
                    if (newx,newy) not in dist or newedge < dist[(newx,newy)]:
                        dist[(newx,newy)] = newedge
                        heapq.heappush(heap,(newedge,(newx,newy)))
        #print(dist)
        #print("hello")
        return dist[(target)]