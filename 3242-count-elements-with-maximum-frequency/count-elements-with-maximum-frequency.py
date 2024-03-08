class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        maxm = max(Counter(nums).values())
        ans = 0
        for i in Counter(nums):
            if Counter(nums)[i]==maxm:ans +=Counter(nums)[i]
        return ans
        