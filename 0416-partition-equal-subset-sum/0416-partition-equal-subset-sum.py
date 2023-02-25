class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo = {}
        def rec(subsetsum,index):
            if index>= len(nums):
                return
            if subsetsum <0:
                return
            if (subsetsum,index) in memo:
                return memo[(subsetsum,index)]
            if subsetsum == 0:
                return True
            res = rec(subsetsum-nums[index],index+1) or rec(subsetsum,index+1)  
            memo[(subsetsum,index)] = res
            return res
        if sum(nums)%2==1:
            return False
        half = math.ceil(sum(nums)/2)
        return rec(half,0)
        # dp = [False for i in range(200001)]
        # dp[0] = True
        # for num in nums:
        #     for i in range(half,0,-1):
        #         if i>=num:
        #             dp[i] = dp[i-num] or dp[i]
        # return dp[half]
        