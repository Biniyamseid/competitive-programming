class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # start from the second heighest
        # if min(nums)<k:retrun -1
        # then go if k in nums n-2 -0 -1 else n-2 -0
        if min(nums)<k:
            return -1
        count = len(set(nums))
        if k in nums:
            return count-1
        else:
            return count
        
        