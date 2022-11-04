class Solution:
    def countPrimes(self, n: int) -> int:
        if n<2:
            return 0
        is_prime = [True for _ in range(n)]
        #print(is_prime)
        is_prime[0] = is_prime[1] = False
        for i in range(2,n):
            if i*i >= n:
                break
            if is_prime[i]:
                for j in range(i*i,n,i):
                    is_prime[j] = 0
        return sum([1 for i in is_prime if i])
        