class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        right = n-1
        left = 0
        while left<right:
            mid = (left+right)//2
            if nums[mid]>nums[right]:
                left = mid +1
            elif nums[mid]< nums[left]:
                right = mid
            else:
                right-=1
        return nums[left]

            
            
                
            
        