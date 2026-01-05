class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        minm = float(inf)
        total = 0
        count = 0
        for i in  range(len(matrix)):
         for j in range(len(matrix[0])):
            curr = matrix[i][j]
            minm = min(minm,abs(curr))
            if curr<=0:
                count +=1
            total+=abs(curr)
        if count%2!=0:
                total-= 2*minm
        return total
            

        