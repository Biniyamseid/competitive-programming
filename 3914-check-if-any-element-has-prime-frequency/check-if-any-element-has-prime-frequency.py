class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        #find frequency
        #and check if the frequency of the numbers is prime
        def is_prime(n):
            if n <= 1:
                return False
            if n == 2:
                return True
            if n % 2 == 0:
                return False
            for i in range(3, int(n ** 0.5) + 1, 2):
                if n % i == 0:
                    return False
            return True
        count = Counter(nums)
        freqs = [j for i,j in count.items() ]
        answer = False
        for i in freqs:
            if  is_prime(i):
                answer = True
        return answer
                