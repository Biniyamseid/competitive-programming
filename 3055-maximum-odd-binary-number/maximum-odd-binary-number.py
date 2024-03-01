class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count = Counter(s)['1']
        if count==0:
            return s
        if count <2:
            l = len(s)
            return '0'*(l-1)+'1'
        n = len(s)-count
        k = count-1
        return '1'*k+'0'*n+'1'
        