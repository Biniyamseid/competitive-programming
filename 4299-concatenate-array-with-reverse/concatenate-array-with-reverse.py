class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        ans = nums.copy()
        return ans+ans[::-1]