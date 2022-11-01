class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        grid = heights
        heap = [(0,(0,0))]
        min_cost = defaultdict(lambda:float("inf"))
        target = (len(heights)-1,len(heights[0])-1)
        while heap:
            cost,coordinate = heapq.heappop(heap)
            n,m = coordinate
            if coordinate == target:
                break
            directions = [(0,1),(1,0),(0,-1),(-1,0)]
            for p,q in directions:
                newX,newY = p+n,q+m
                if newX >= 0 and newX<=len(grid)-1 and newY>=0 and newY <= len(grid[0])-1:
                    max_abs_difference_so_far_in_this_path = max(cost,abs(grid[n][m]-grid[newX][newY]))
                    if (newX,newY) not in min_cost or min_cost[(newX,newY)] > max_abs_difference_so_far_in_this_path:
                    #ከዚህ በፊት በሌላ መንገድ መጥቶ ነበረ አሁን ደግሞ በሌላ መንገድ ሲመትጣ ትንሹን እናስቀምጥለት
                        min_cost[(newX,newY)] = min(max_abs_difference_so_far_in_this_path,min_cost[(newX,newY)])
                        heapq.heappush(heap,(max_abs_difference_so_far_in_this_path,(newX,newY)))
        #print(min_cost)
        return min_cost[target] if min_cost[target] != float("inf") else 0
            