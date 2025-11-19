class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums.sort()
        for num in nums:
            if original==num:
                original *= 2
        return original 
        