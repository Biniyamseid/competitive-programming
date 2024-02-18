class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        di = {}
        for i,val in enumerate(nums):
            if target-val in di:
                return [di[target-val],i]
            di[val]=i