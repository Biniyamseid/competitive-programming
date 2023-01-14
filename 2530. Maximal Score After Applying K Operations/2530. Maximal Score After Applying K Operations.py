class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        import heapq
        """
        every time take the maximum value.
        """
        import heapq
        nums.sort(reverse = True)
        score = 0
        heap = [-i for i in nums]
        for i in range(k):
            val = abs(heapq.heappop(heap))
            score += val
            heapq.heappush(heap,-math.ceil(val/3) )
        return score