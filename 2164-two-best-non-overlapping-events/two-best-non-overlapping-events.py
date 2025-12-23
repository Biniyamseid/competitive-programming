import heapq
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        heap = []
        ans = 0
        best = 0
        for s,e,v in events:
            
            while heap and heap[0][0] < s:
                e1,v1 = heapq.heappop(heap)
                best = max(best,v1)
            ans = max(ans,best+v)
            heapq.heappush(heap,(e,v))
        return ans


