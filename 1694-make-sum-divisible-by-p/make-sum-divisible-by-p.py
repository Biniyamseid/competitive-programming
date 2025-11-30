class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        # ml = float(inf)
        # total = sum(nums)
        # if total%p == 0:
        #     return 0
        # for i in range(len(nums)):
        #     for j in range(i,len(nums)):
        #         curr = nums[i:j+1]
        #         if len(curr)!= len(nums) and (total - sum(curr))%p ==0:
        #             ml = min(ml,len(curr))
        # return ml if ml!=float(inf) else -1
        # # options find maximum sum divisible by k
        if sum(nums)%p==0:
            return 0
        rolling_sum = 0
        total = sum(nums)
        focus = total%p
        seen = {0:-1}
        answer = len(nums)
        got_first = False
        prefix_sum = []
       

        for i in range(len(nums)):
            rolling_sum = (rolling_sum + nums[i])%p
            target = (rolling_sum - focus+p)%p
            if target in seen:
                j = seen[target]
                if i-j < answer:
                    answer = i-j
            seen[rolling_sum]= i
        return answer if answer!=len(nums) else -1



                

        