class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        n = numRows
        res = []
        for i in range(n):
            res.append([1]*(i+1))

        def recur(i):
            if i>=n:
                return 
            for j in range(i):
                if j == 0:
                    pass
                else:
                    res[i][j] = res[i-1][j-1]+res[i-1][j]
            recur(i+1)
        recur(2)
        print(res)
        return res
    
        