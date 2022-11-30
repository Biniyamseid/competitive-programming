class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        minimum = float("inf")
        while l <= r:
            mid = (l+(r-l)//2)
            minimum = min(minimum,nums[mid])
            if nums[l] <= nums[mid]:
                minimum = min(minimum,nums[l])
                l = mid +1
            else:
                r = mid - 1
        return minimum
            
        