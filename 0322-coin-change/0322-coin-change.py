class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def mincoin(amount):
            if amount in memo:
                return memo[amount]
            if amount == 0:
                return 0
            if amount <0:
                return float("inf")
            memo[amount] = min([1+ mincoin(amount-i) for i in coins])
            return memo[amount]
        val = mincoin(amount)
        return val if val != float("inf") else -1
    
        
            