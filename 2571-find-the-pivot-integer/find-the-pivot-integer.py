class Solution:
    def pivotInteger(self, n: int) -> int:
        total = sum([i for i in range(1,n+1)])
        s = 0
        for i in range(1,n+1):
            if s==(total-i)/2:
                return i
            s+=i
        if s==total//2-n:
            return n
        return -1
        

        