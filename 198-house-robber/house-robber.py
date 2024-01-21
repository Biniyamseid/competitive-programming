class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return max(nums)
        dp = nums[:2]
        dp[1] = max(dp)
        for i in range(2,len(nums)):
            cur = max(dp[i-2]+nums[i],dp[i-1])
            dp.append(cur)
        print(dp)
        return max(dp[-1],dp[-2])
        