class Solution:
    def getSum(self, a: int, b: int) -> int:
        def get_bin(x,y):
            x = list(str(bin(x)))
            y = list(str(bin(y)))
            x.remove('b')
            y.remove('b')
            return (x,y)
        x,y = get_bin(a,b)
        result = []
        j = 0
        carry =0
        for i in range():
            temp = int(y[j]) + int(i)+int(carry)
            if temp ==0:
                res = 0
                carry = 0
            elif temp == 1:
                res = 1
                carry = 0
            elif temp == 2:
                res = 0
                carry = 1
            elif remp == 3:
                res = 1
                carry = 1
            result.append(res)
            j -= 1
            i -= 1
        print(result)
        
