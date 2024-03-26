class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s = set(nums)
        for i in range(1,1000000):
            if i not in s:
                return i
        return float("inf")

        