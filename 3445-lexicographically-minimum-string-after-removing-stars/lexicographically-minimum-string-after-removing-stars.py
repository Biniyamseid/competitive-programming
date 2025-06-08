import heapq
class Solution:
    def clearStars(self, s: str) -> str:
        removed_list = []
        heap = []
        heapq.heapify(heap)
        for idx,val in enumerate(s):
            if val != "*":
                heapq.heappush(heap,[ord(val),-idx])
            if val == "*" and heap:
                vals = heapq.heappop(heap)
                removed_list.append(vals)
        # print(heap)
        # print(removed_list)
        removed_indices = set([i for j,i in removed_list if removed_list])
        word = ""
        for idx,val in enumerate(s):
            if val == "*":
                pass
            elif -1*idx in removed_indices:
                pass
            else:
                word+=val
        return word




        