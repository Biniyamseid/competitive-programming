class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        n = numRows
        res = []
        for i in range(n):
            res.append([1]*(i+1))
            
        print(res)
        for i in range(2,n):
            for j in range(i):
                if j == 0:
                    pass
                else:
                    res[i][j] = res[i-1][j-1]+res[i-1][j]
        print(res)
        return res
    
        