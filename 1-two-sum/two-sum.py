class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dj = {}
        for i,j in enumerate(nums):
            if target-j in dj:
                return [dj[target-j],i]
            dj[j] = i
        return -1