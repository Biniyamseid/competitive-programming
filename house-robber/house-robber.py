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
        nums[1] = max(nums[0],nums[1])
        for i in range(2,len(nums)):
            nums[i] = max(nums[i-1],nums[i-2]+nums[i])
        return max(nums[-1],nums[-2])
            
            
        