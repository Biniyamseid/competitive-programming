class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        return len(nums)-1 if not(sum(nums)%2) else 0



        