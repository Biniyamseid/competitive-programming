class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:
        answer = 0
        n,r = min(n,int(str(n)[::-1])),max(n,int(str(n)[::-1]))
        primes = [True for i in range(r+1)]
        primes[0]=0
        primes[1]=0
        for i in range(2,int((r+1)**0.5)+1):
            if primes[i]:
                for j in range(i*i,r+1,i):
                    primes[j]=False
        for k in range(n,r+1):
            if primes[k]:
                answer+=k
        return answer
        

       