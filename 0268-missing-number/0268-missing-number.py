class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        mis = 0
        for i in range(len(nums)+1):
            mis ^= i
        for j in nums:
            mis ^= j
        return mis
        
        

        
        