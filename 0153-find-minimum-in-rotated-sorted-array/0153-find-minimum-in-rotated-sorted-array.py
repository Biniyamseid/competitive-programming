class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        minimum = nums[0]
        while l <= r:
            mid = (l+(r-l)//2)
            minimum = min(minimum,nums[mid])
            if nums[mid] >= nums[r]:
                l = mid +1
            else:
                r = mid -1
        return minimum
            
        