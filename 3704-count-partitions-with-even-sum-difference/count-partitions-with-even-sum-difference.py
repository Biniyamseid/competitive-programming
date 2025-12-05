class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        result = 0
        total = sum(nums)
        even = not (total%2)
        prefix = 0
        if even:
            return len(nums)-1
        else:
            return 0
        for idx,num in enumerate(nums):
            if idx==len(nums)-1:
                break
            prefix+=num
            if even:
                result+=1
            # if ((2*prefix)-total)%2==0:
            #     result+=1
            # if  ((prefix)-(total-prefix))%2 ==0:
            #     result+=1
        return result


        