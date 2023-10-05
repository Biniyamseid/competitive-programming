class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left = 0
        n = len(nums)
        right = n-1
        if len(nums)<=10:
            return min(nums)
        while left<=right:
            mid=(left+right)//2
            if mid == 0:
                if nums[mid+1]>=nums[mid]<=nums[-1]:
                        return nums[mid]
                if nums[mid]>nums[-1]:
                    left = mid+1
                else:
                    return nums[mid]
            elif mid == n-1:
                if nums[0]>=nums[mid]<=nums[mid-1]:
                    return nums[mid]
                if nums[mid]<nums[0]:
                    left = mid+1
                else:
                    return nums[0]
            elif nums[mid-1]>=nums[mid]<=nums[mid+1]:
                return nums[mid]
            elif nums[mid-1]<=nums[mid]>=nums[mid+1]:
                return nums[mid+1]
                
            elif nums[mid]>nums[0]:
                left = mid+1
            else:
                right = mid-1
        
                
            
        
        