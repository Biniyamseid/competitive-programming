class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7
        
        # Base case
        typeA = 6  # all 3 colors different
        typeB = 6  # first and third same
        
        for _ in range(2, n + 1):
            newA = (2 * typeA + 2 * typeB) % MOD
            newB = (2 * typeA + 3 * typeB) % MOD
            typeA, typeB = newA, newB
        
        return (typeA + typeB) % MOD