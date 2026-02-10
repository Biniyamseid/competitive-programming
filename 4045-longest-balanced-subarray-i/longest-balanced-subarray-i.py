class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        # mamualatation streak
        max_len = 0

        for i in range(len(nums)):
            odd = {}
            even = {}

            for j in range(i, len(nums)):
                if nums[j] & 1:
                    odd[nums[j]] = odd.get(nums[j], 0) + 1
                else:
                    even[nums[j]] = even.get(nums[j], 0) + 1

                if len(odd) == len(even):
                    max_len = max(max_len, j - i + 1)

        return max_len