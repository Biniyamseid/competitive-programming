class Solution:
    def fib(self, n: int) -> int:
        memo = {}
        
        
        def fibonanci(n):
            if n ==0:
                return 0
            if n<=2:
                return 1
            if n in memo:
                return memo[n]
            result = fibonanci(n-1)+fibonanci(n-2)
            memo[n] = result
            return memo[n]
        return fibonanci(n)
        