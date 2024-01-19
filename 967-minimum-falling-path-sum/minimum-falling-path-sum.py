class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        @cache
        def ans(i,j):
            if i==len(matrix[0]):
                return 0
            if i<0 or j<0 or j>=len(matrix[0]):
                return float(inf)
            direction = [(1,0),(1,1),(1,-1)]
            res = float(inf)
            for r,c in direction:
                res = min(res,matrix[i][j]+ans(i+r,j+c))
            return res
        result = float(inf)
        for i in range(len(matrix[0])):
            result = min(result,ans(0,i))
            print(result)
        return result

