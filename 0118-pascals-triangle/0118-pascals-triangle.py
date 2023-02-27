class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        n = numRows
        res = []
        for i in range(n):
            res.append([1]*(i+1))

        def recur(i):
            if i<2:
                recur(i+1)
            if i>=n:
                return 
            for j in range(i):
                if j!= 0:
                    res[i][j] = res[i-1][j-1]+res[i-1][j]
            return recur(i+1)
        recur(0)
        print(res)
        return res
    
        