class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        """5 5 5"""
        nums.sort()
        ans = -1
        previous = 0
        for i in range(2):
            previous+=nums[i]
        for i in range(2,len(nums)):
            if previous>nums[i]:
                ans = previous+nums[i]
            previous+=nums[i]
        return ans

        