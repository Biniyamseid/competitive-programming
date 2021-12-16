class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        l = []
        nums.sort()
        n = len(nums)
        for i in range(n):
            if nums[i] == target:
                l.append(i)
        return l
