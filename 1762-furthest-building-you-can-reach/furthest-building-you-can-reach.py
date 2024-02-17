class revl(list):
    def append(self,val):
        super().append(val)
        self.sort(reverse=True)
import heapq
class Solution:
    def furthestBuilding(self, heights: List[int], b: int, l: int) -> int:
        heap = []
        for i in range(len(heights)-1):
            diff = heights[i+1]-heights[i]
            if diff>0:
                heapq.heappush(heap,diff)
                if len(heap)>l:
                    b-=heapq.heappop(heap)
                if b<0:
                    return i
        return len(heights)-1

        