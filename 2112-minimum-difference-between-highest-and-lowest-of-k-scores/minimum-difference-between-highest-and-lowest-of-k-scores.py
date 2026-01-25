class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        minm = inf
        for i in range(len(nums)-k+1):
            minm= min(nums[i+k-1]-nums[i],minm)
        return minm

        