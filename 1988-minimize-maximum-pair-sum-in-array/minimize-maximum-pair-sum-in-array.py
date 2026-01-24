class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        # sort [2,3,3,5] then pair first to end and return the max
        maxm = -inf
        nums.sort()
        for i in range(len(nums)//2):
            maxm = max(nums[i]+nums[len(nums)-i-1],maxm)
        return maxm

        