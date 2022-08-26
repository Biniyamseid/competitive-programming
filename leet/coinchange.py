class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [float("inf") for i in range(amount+1)]
        dp[0] = 0
        for i in range(amount+1):
            for coin in coins:
                if i-coin >= 0:
                    dp[i] = min(dp[i],1+dp[i-coin])

        return dp[amount] if dp[amount] != float("inf") else -1
a = Solution()
print(a.coinChange([1,2,5],11))

