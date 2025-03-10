class Solution:
    def maxScore(self, nums: List[int]) -> int:
        """
        nums = [2,4,8,16]  -> ans = 64
         nums = [1,2,3,4,5] -> 64
         first find lcm then find gcd and try to find gcd by removing the least element and return the maximum
        
        """
        res = 0
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]**2
        import math
        for i in range(-1,len(nums)):
            d = 0
            m=1
            for j in range(len(nums)):
                if i!=j:
                    d = math.gcd(d,nums[j])
                    m = math.lcm(m,nums[j])
            res = max(res,d*m)
        return res

        
        # gcd = math.gcd(*nums)
        # lcm = math.lcm(*nums)
        # gcd2 = 0
        # if len(nums)>1:
        #     nums = sorted(nums)
        #     nums.pop(0)
            
        # gcd2 = math.gcd(*nums)
        # lcm2 = math.lcm(*nums)
        # answer = max(lcm*gcd,lcm2*gcd2)
        # return max(answer,res)
        