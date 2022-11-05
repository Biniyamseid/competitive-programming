class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        if len(nums) ==1:
            return nums[0]
        dp=[nums[0],max(nums[0],nums[1])]
        for i in range(2,len(nums)):
            dp.append(0)
            dp[i] = max(dp[i-1],nums[i]+dp[i-2])
        return dp[-1]
        """
        if len(nums) ==1:
            return nums[0]
        memo = {0:nums[0],1:max(nums[0],nums[1])}
        
        def dfs(i):
            if i in memo:
                return memo[i]
            if i>len(nums):
                return 0
            if i< 0:
                return 0
            memo[i] = max(dfs(i-1),nums[i] + dfs(i-2))
            return memo[i]
        return dfs(len(nums)-1)
            
            
        