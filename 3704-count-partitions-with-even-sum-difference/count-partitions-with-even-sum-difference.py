class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        result = 0
        total = sum(nums)
        prefix = 0
        for idx,num in enumerate(nums):
            if idx==len(nums)-1:
                break
            prefix+=num
            if  ((prefix)-(total-prefix))%2 ==0:
                result+=1
        return result


        