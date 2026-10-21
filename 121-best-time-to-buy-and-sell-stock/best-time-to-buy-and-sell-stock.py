class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # dp = [minm,maxprofit]
        dp = [prices[0],0]
        for i in range(len(prices)):
            dp = [min(dp[0],prices[i]),max(dp[1],prices[i]-dp[0])]
        return dp[1]


       
            
        