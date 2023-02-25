class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2==1:
            return False
        half = math.ceil(sum(nums)/2)
        dp = [False for i in range(200001)]
        dp[0] = True
        for num in nums:
            for i in range(half,0,-1):
                if i>=num:
                    dp[i] = dp[i-num] or dp[i]
        return dp[half]
        